# DNSSEC_Impact_Analysis

DATA DRIVEN IMPACT ANALYSIS OF DNSSEC OUTAGES

The goal of this data analytics capstone project is to develop a comprehensive, data-driven system to evaluate and address the impacts of DNSSEC (Domain Name System Security Extensions) outages during natural disasters and other adverse conditions.


## Authors

- Neha Reddy Gutha
- Naga Sai Dhanya Veerepalli
- Peiran Li
- Yashwanth Penugonda
- Gokul Krishna Reddy Gaddam

## Overview

This repository contains the code artifacts for analyzing DNS server outages, building predictive models, and examining correlations between natural disasters and server availability. This project focuses on the Indonesian DNS infrastructure to evaluate resiliency during natural disasters such as earthquakes and tsunamis.

Note: The datasets used in this project are not included in the repository. For public datasets, links have been provided below.

## Repository Structure

1. modeling
  
   Contains scripts for data preprocessing, feature engineering, and machine learning model development.
   Includes models such as Random Forest, Gradient Boosting, and Logistic Regression for predicting DNS server outages.

2. disaster_outage_analysis

   Contains scripts for analyzing correlations between natural disasters and DNS server outages.
   Focuses on visualizations and geospatial analysis of server availability during events like earthquakes and tsunamis.

4. utils

   Contains utility scripts and helper functions used across the project.

## Data Sources

The data used for this project is sourced from reliable open sources and is not included in this repository.

DNS Data: INSO - GMU
Natural Disaster Data: NOAA, GeoLite2, Indonesian Disaster Data - BNPB

## Dependencies

To run the scripts in this repository, the following libraries and tools are required:

Programming Language: Python 3.8+

Core Libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- geopandas
- folium
- pyspark

## How to Run

1. Setting up the Environment
Clone the repository:
```git clone https://github.com/<username>/dns-resiliency-analysis.git```
```cd dns-resiliency-analysis```

2. Install required Python libraries:
```pip install -r requirements.txt  ```

3. Run Machine Learning Models
Navigate to the modeling folder and execute the scripts:

```python data_preprocessing.py  ```
```python feature_selection.py  ```
```python random_forest_model.py  ```
```python model_evaluation.py```

4. Run Disaster-Outage Analysis
To analyze correlations and visualize outages during disasters, run:

```python disaster_correlation_analysis.py ``` 
```python outage_visualization.py  ```

5. For geospatial mapping, use the Jupyter Notebook:

```jupyter notebook server_outage_maps.ipynb ``` 


## Acknowledgements
1. Osterweil, Eric, Pouyan Fotouhi Tehrani, Thomas C. Schmidt, and Ma hias Wählisch. "From the beginning: Key transi ons in 
the first 15 years of DNSSEC." IEEE Transac ons on Network and Service Management 19, no. 4 (2022): 5265-5283. 

2. Osterweil, Eric, Dan Massey, and Lixia Zhang. "Deploying and monitoring dns security (dnssec)." In 2009 Annual Computer 
Security Applica ons Conference, pp. 429-438. IEEE, 2009. 

3. Jain, B., Daing, C., Dunaboyina, D., Idris, H., Franzine , L., Pa , T., “Data-Driven Impact Analysis of DNSSEC Outages,” 
presented at the Spring 2024 DAEN 690 Capstone Presenta on Showcase, Fairfax, Virginia, April 30, May 3, & May 6, 2024.



## 🛠 Skills
Data Mining, Data Engineering, Data Visualization, Machine Learning, Systems Engineering, DevSecOps.

