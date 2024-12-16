#!/bin/bash

# Step 1: Log into VPN and extract data from the database
echo "Logging into VPN and extracting data from the database..."
sshpass -p 'password' ssh -T user@sr2s1.mesa.gmu.edu << EOF
  echo "Running SQL query on the database..."
  mysql -u daen690 -p'database password' -h sr3s14.mesa.gmu.edu -P 4439 --batch --skip-column-names -e \
  "SELECT ns.*, ks.ID AS KS_ID, ks.NS_ID AS KS_NS_ID, ks.SET_ID AS KS_SET_ID, ks.SEEN AS KS_SEEN, ks.AVG_RTT_MILLIS AS KS_AVG_RTT_MILLIS, ks.SUCCEEDED AS KS_SUCCEEDED, ks.SMALLEST_BUFF AS KS_SMALLEST_BUFF, ks.LARGEST_BUFF AS KS_LARGEST_BUFF, ks.LARGEST_MSG AS KS_LARGEST_MSG, ks.TCP_AVAIL AS KS_TCP_AVAIL, ks.SET_INCEP AS KS_SET_INCEP, ks.SET_EXP AS KS_SET_EXP FROM secspider.SS_NAMESERVER ns JOIN secspider.SS_KEY_STATS ks  ON ns.ID = ks.NS_ID WHERE
  SUBSTRING_INDEX(SUBSTRING_INDEX(ns.NAME, '.', -2), '.', 1) = 'id' limit 1000000;" > /data/home/ypenugon/indo_ns_ks.csv
  exit
EOF

# Step 2: Copy the CSV file from the VPN machine to local machine
echo "Copying CSV file from VPN to local machine..."
sshpass -p 'password' scp user@sr2s1.mesa.gmu.edu:location/indo_ns_ks.csv /destination/indo_ns_ks.csv

# Step 3: Upload the file to S3
echo "Uploading the file to S3..."
aws s3 cp /Users/yashwanthp/Downloads/DAEN690_Data/indo_ns_ks.csv s3://insighterss3/Indonesia_outages_analysis/indo_ns_ks.csv --region us-east-1 --profile profile

echo "Process completed."
