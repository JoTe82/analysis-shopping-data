"""
Data Validation: customer_shopping_data.csv

Data Source: The dataset used, "Customer Shopping Dataset – Retail Sales Data",  
was obtained from the platform Kaggle.com and is published under the  
Creative Commons CC0 1.0 Universal (Public Domain Dedication) license.  
The authors have waived all copyright and related rights to this data.

License details: https://creativecommons.org/publicdomain/zero/1.0/deed.en
"""

# pandas import
import pandas as pd

# display all columns of the DataFrame
pd.set_option("display.max_columns", None)

# a function for output with spacing
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

# basic statistical overview
print_spaced(data.describe(include="all"))

# convert column names to a list
column_titles = data.columns.to_list()
print_spaced(column_titles)

# count values in each column (descending) to detect anomalies
for i in column_titles:
    print_spaced(data[i].value_counts(ascending=False))

# check for missing values (NaNs)
if data.isnull().any(axis=None):
    print("The DataFrame contains NaN values:")
    print_spaced(data[data.isnull().any(axis=1)])  
else:
    print_spaced("No NaN values were found.")

# check for duplicated rows
if data[data.duplicated()].any(axis=None):
    print("Duplicated rows were found:")
    print_spaced(data[data.duplicated()])
else:
    print_spaced("No duplicated rows were found.")

# final output
print(f"{'Data validation finished':*<60}")

