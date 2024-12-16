from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, PCA
from pyspark.ml.classification import LinearSVC
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType  # Add this import
from pyspark.ml.classification import LinearSVC
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.sql.functions import col
from pyspark.sql import functions as F
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from pyspark.sql.functions import udf
from pyspark.sql.types import LongType

from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#     .appName("Jupyter Notebook with Increased Memory") \
#     .config("spark.hadoop.fs.s3a.access.key", "ASIATCKATABJPYAQRUUJ") \
#     .config("spark.hadoop.fs.s3a.secret.key", "RufbPxqbOywzLZ+I/LCAtphTR6GmFN9OjS/eO4Iw") \
#     .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
#     .getOrCreate()
spark = SparkSession.builder.appName("Jupyter Notebook with Increased Memory").config("spark.executor.memory", "8g").config("spark.driver.memory", "8g").config("spark.memory.fraction", "0.8").config("spark.executor.instances", "4").getOrCreate()



ip_data_path = "/user/hadoop/country.csv"

# Read Parquet file into DataFrame
ip_data = spark.read.csv(ip_data_path,sep=",",header=True)

# ns_data_path = "/Users/yashwanthp/Downloads/DAEN690_Data/indo_ns_full.csv"
ns_data_path = "s3://insighterss3/Indonesia_outages_analysis/indo_ns_full.csv"  # Replace with the correct file path
data = spark.read.csv("s3a://your-bucket/indo_ns_full.csv", sep="\t", header=False)
columns = ["NS_ID", "ZONE_ID", "NAME", "IP"]
ns_data = spark.read.csv(ns_data_path,sep="\t",header=False)
ns_data = ns_data.toDF(*columns)

from pyspark.sql.functions import col

# Filter to exclude rows with 'NULL' as a string and keep only valid IPv4 addresses
ip_data = ip_data.filter(
    col("start_ip").rlike(r"^\d{1,3}(\.\d{1,3}){3}$") &
    col("end_ip").rlike(r"^\d{1,3}(\.\d{1,3}){3}$") &
    (col("start_ip") != 'NULL') &
    (col("end_ip") != 'NULL')  # Exclude rows where 'NULL' is a string
)

# UDF to convert IP to numeric
def ip_to_long(ip):
    if ip == 'NULL' or ip is None:
        return None  # Handle 'NULL' or None explicitly
    parts = ip.split(".")
    return int(parts[0]) * 256**3 + int(parts[1]) * 256**2 + int(parts[2]) * 256 + int(parts[3])

ip_to_long_udf = udf(ip_to_long, LongType())

# Apply the IP conversion to numeric values
ip_data = ip_data.withColumn("start_ip_numeric", ip_to_long_udf("start_ip"))
ip_data = ip_data.withColumn("end_ip_numeric", ip_to_long_udf("end_ip"))

# Filter out rows with invalid start_ip_numeric or end_ip_numeric
ip_data = ip_data.filter(col("start_ip_numeric").isNotNull() & col("end_ip_numeric").isNotNull())

# Apply the IP conversion to ns_data as well
ns_data = ns_data.withColumn("ip_numeric", ip_to_long_udf("IP"))

# Filter out rows with invalid IPs in ns_data
ns_data = ns_data.filter(col("ip_numeric").isNotNull())

# Join the two datasets
joined_data = ns_data.join(
    ip_data,
    (ns_data["ip_numeric"] >= ip_data["start_ip_numeric"]) &
    (ns_data["ip_numeric"] <= ip_data["end_ip_numeric"]),
    "inner"
)

# Filter for rows where the country is 'ID' (Indonesia) and count the rows
indonesia_count = joined_data.filter(col("country") == "ID").count()

# Print the result
print(f"Number of rows from Indonesia: {indonesia_count}")

indonesia_data = joined_data.filter(col("country") == "ID")
indonesia_data.write.parquet("s3://insighterss3/Indonesia_outages_analysis/indo_ns_ip")