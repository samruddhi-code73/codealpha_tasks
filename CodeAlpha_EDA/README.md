# Amazon Products Exploratory Data Analysis (EDA)

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on an Amazon sales dataset obtained from Kaggle. The analysis was performed using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

The main goal of this project is to identify trends, patterns, anomalies, and insights related to product pricing, ratings, discounts, and customer behavior.

# Objectives

* Understand the dataset structure
* Clean and preprocess the data
* Identify missing values and anomalies
* Analyze pricing and discount trends
* Explore product ratings and customer behavior
* Detect outliers in product prices
* Generate meaningful business insights
* Visualize data using charts and graphs

# Dataset Information

Dataset Source: Kaggle Amazon Sales Dataset

### Important Columns

* product_name
* category
* actual_price
* discounted_price
* discount_percentage
* rating
* rating_count

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* VS Code

# Data Cleaning Steps

The following preprocessing steps were performed:

* Removed currency symbols from price columns
* Removed commas from numerical values
* Converted object datatypes into numeric datatype
* Handled missing values
* Removed duplicate records
* Fixed encoding issues
* Converted rating columns into float datatype

# Exploratory Data Analysis Performed

The following analyses were performed:

* Distribution of product ratings
* Distribution of discount percentage
* Product category analysis
* Correlation analysis
* Outlier detection using boxplot
* Top-rated products analysis
* Highest discount products analysis

# Visualizations Used

* Histogram
* Bar Chart
* Boxplot
* Correlation Heatmap

# Key Insights

* Most products are rated between 4.0 and 4.5
* Electronics categories dominate the dataset
* Significant price outliers exist
* Higher discounts do not necessarily improve ratings
* Most products receive positive customer feedback

# Correlation Analysis

Correlation between discount percentage and product ratings:
-0.155

### Interpretation

A weak negative correlation exists between discount percentage and ratings. This indicates that higher discounts do not significantly improve customer ratings.

# Challenges Faced

* Encoding issues in currency symbols
* Handling missing values
* Converting price columns into numeric datatype
* Managing outliers in pricing data

# Future Scope

This project can be extended further by:

* Building recommendation systems
* Performing sentiment analysis
* Creating Power BI/Tableau dashboards
* Predicting product ratings using Machine Learning

# How to Run the Project

## Run EDA Script

python eda.py

## Run Visualization Script

python charts.py

# Final Outcome

This project successfully demonstrated practical implementation of Exploratory Data Analysis using Python. The analysis helped identify pricing patterns, customer behavior, discount trends, and data anomalies within Amazon product data.

# Author

Samruddhi Bhowood
