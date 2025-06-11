"""
Statistical analysis of quantitative values: customer_shopping_data.csv

Data Source: The dataset used, "Customer Shopping Dataset – Retail Sales Data",  
was obtained from the platform Kaggle.com and is published under the  
Creative Commons CC0 1.0 Universal (Public Domain Dedication) license.  
The authors have waived all copyright and related rights to this data.

License details: https://creativecommons.org/publicdomain/zero/1.0/deed.en
"""

# import of statistics, numpy, pandas, matplotlib
# and the self-created module stats_evaluation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stats_evaluation

# display all columns of the DataFrame
pd.set_option("display.max_columns", None)

# a function for an output with spacing
def print_spaced(i):
    print(i)
    print()

# data import from the dataset customer_shopping_data.csv
data = pd.read_csv("customer_shopping_data.csv")

# output of the first 10 rows
print_spaced(data.head(10))

# summary of the DataFrame structure
data.info()
print()

# looking for correlations
print_spaced(data.corr(numeric_only=True))

# creating a DataFrame with statistical analysis for the entire dataset
data_complete = stats_evaluation.stats(data)
print("The statistical analysis for the entire dataset:")
print_spaced(data_complete)

# a statistical analysis for each shopping mall
mall = list(data["shopping_mall"].unique())

# a for-loop to execute the statistical analysis for each shopping mall
for i in mall:
    mall_df = data[data["shopping_mall"] == i]
    mall_df = stats_evaluation.stats(mall_df)
    print("The statistical analysis for the shopping mall " + str(i) + ":")
    print_spaced(mall_df)
    # mall_df.to_excel(str(i)+"_stats_customer_shopping_data.xlsx")

# Findings: the mode of the variables age, quantity, and price varies across all shopping malls
# therefore, separate histograms will be created for each shopping center to visually compare these differences

# to provide a baseline for comparison, the modes of the entire dataset are visualized first
figur, achsen = plt.subplots(1,3, figsize=(24, 6), squeeze=False)
figur.suptitle("Histograms of the “age”, “quantity” and “price” column for the entire dataset")
index = 0

# center histograms with integer bins
bins = np.arange(1, 7) - 0.5

# for column “age” of the entire dataset
achsen[0][0].hist(data["age"])
achsen[0][0].set_xticks(range(15,71,5),labels=range(15,71,5), size=10)
achsen[0][0].set_xlabel("age")
achsen[0][0].set_ylabel("Frequency")

# for column “quantity” of the entire dataset
achsen[0][1].hist(data["quantity"], bins=bins)
achsen[0][1].set_xticks(range(1,6,1),labels=range(1,6,1), size=10)
achsen[0][1].set_xlabel("quantity")
achsen[0][1].set_ylabel("Frequency")

# for column “price” of the entire dataset
achsen[0][2].hist(data["price"])
achsen[0][2].set_xticks(range(0,5250,1000),labels=range(0,5250,1000), size=10)
achsen[0][2].set_xlabel("Price")
achsen[0][2].set_ylabel("Frequency")

# visualization of modes for each shopping center
figur, achsen = plt.subplots(2,5, figsize=(24, 6), squeeze=False)
figur.suptitle("Histograms of the “age” column for each shopping center")
figur.subplots_adjust(wspace=0.25,hspace=0.4)
# for the column age
index = 0
for row in range(2):
    for col in range(5):
        mall_age = data[data["shopping_mall"] == mall[index]]
        achsen[row][col].hist(mall_age["age"])
        achsen[row][col].set_title(mall[index])
        achsen[row][col].set_xticks(range(15,71,5),labels=range(15,71,5), size=10)
        achsen[row][col].set_xlabel("age")
        achsen[row][col].set_ylabel("Frequency")
        index = index + 1

# for the column quantity
figur, achsen = plt.subplots(2,5, figsize=(24, 6), squeeze=False)
figur.suptitle("Histograms of the “quantity” column for each shopping center")
figur.subplots_adjust(wspace=0.25,hspace=0.5)
index = 0
for row in range(2):
    for col in range(5):
        mall_quantity = data[data["shopping_mall"] == mall[index]]
        achsen[row][col].hist(mall_quantity["quantity"], bins=bins)
        achsen[row][col].set_title(mall[index])
        achsen[row][col].set_xticks(range(1,6,1),labels=range(1,6,1), size=10)
        achsen[row][col].set_xlabel("quantity")
        achsen[row][col].set_ylabel("Frequency")
        index = index + 1

# for the column price
figur, achsen = plt.subplots(2,5, figsize=(24, 6), squeeze=False)
figur.suptitle("Histograms of the “price” column for each shopping center")
figur.subplots_adjust(wspace=0.25,hspace=0.4)
index = 0
for row in range(2):
    for col in range(5):
        mall_price = data[data["shopping_mall"] == mall[index]]
        achsen[row][col].hist(mall_price["price"])
        achsen[row][col].set_title(mall[index])
        achsen[row][col].set_xticks(range(0,5250,1000),labels=range(0,5250,1000), size=10)
        achsen[row][col].set_xlabel("Price")
        achsen[row][col].set_ylabel("Frequency")
        index = index + 1

plt.tight_layout()
plt.show()
