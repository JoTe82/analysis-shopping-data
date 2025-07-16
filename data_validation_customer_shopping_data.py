"""
Data Validation: customer_shopping_data.csv

Data Source: The dataset used, "Customer Shopping Dataset – Retail Sales Data",  
was obtained from the platform Kaggle.com and is published under the  
Creative Commons CC0 1.0 Universal (Public Domain Dedication) license.  
The authors have waived all copyright and related rights to this data.

License details: https://creativecommons.org/publicdomain/zero/1.0/deed.en
"""

# import of pandas
# and the function spacing from the self-created module "output"
import pandas as pd
from output import spacing as sp

# display all columns of the DataFrame
pd.set_option("display.max_columns", None)

# data import from the dataset customer_shopping_data.csv
data = pd.read_csv("customer_shopping_data.csv")

# output of the first 10 rows
sp(data.head(10))

# rename column "price"
data.rename(columns={"price":"sales"}, inplace=True)

# summary of the DataFrame structure
data.info()
print()

# basic statistical overview
sp(data.describe(include="all"))

# convert column names to a list
column_titles = data.columns.to_list()
sp(column_titles)

# count values in each column (descending) to detect anomalies
for i in column_titles:
    sp(data[i].value_counts(ascending=False))

# check for missing values (NaNs)
if data.isnull().any(axis=None):
    print("The DataFrame contains NaN values:")
    sp(data[data.isnull().any(axis=1)])  
else:
    sp("No NaN values were found.")

# check for duplicated rows
if data[data.duplicated()].any(axis=None):
    print("Duplicated rows were found:")
    sp(data[data.duplicated()])
else:
    sp("No duplicated rows were found.")

# final output
print(f"{'Data validation finished':*<60}")

data.to_excel("customer_shopping_data.xlsx")

