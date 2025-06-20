"""
Statistical analysis of quantitative values: customer_shopping_data.csv

Data Source: The dataset used, "Customer Shopping Dataset – Retail Sales Data",  
was obtained from the platform Kaggle.com and is published under the  
Creative Commons CC0 1.0 Universal (Public Domain Dedication) license.  
The authors have waived all copyright and related rights to this data.

License details: https://creativecommons.org/publicdomain/zero/1.0/deed.en
"""

# import of pandas
# and the self-created module stats_evaluation
import pandas as pd
import stats_evaluation

# display all columns of the DataFrame
pd.set_option("display.max_columns", None)

# a function for an output with spacing
def print_spaced(i):
    print(i)
    print()

# data import from the dataset customer_shopping_data.csv
data = pd.read_csv("customer_shopping_data.csv")

# summary of the DataFrame structure
data.info()
print()

# column "invoice_date" will be converted to a datetime data type
data["invoice_date"] = pd.to_datetime(data["invoice_date"], dayfirst=True)
print_spaced("The column \'invoice_date' was converted to a datetime data type.")

# the DataFrame sorted ascending by the column "invoice_date"
# index will be also reseted
data = data.sort_values("invoice_date", ascending=True).reset_index(drop=True)
print_spaced("The DataFrame was sorted ascending by the column \'invoice_date'.")

# output of the DataFrame
print_spaced(data)

# split DataFrame into three, based on the years 2021, 2022 and 2023
# output of the three created DataFrames
data_2021 = data[data["invoice_date"].dt.year == 2021]
print_spaced(data_2021)
data_2022 = data[data["invoice_date"].dt.year == 2022]
print_spaced(data_2022)
data_2023 = data[data["invoice_date"].dt.year == 2023]
print_spaced(data_2023)

# saving of all three new created DataFrames
data_2021.to_csv("customer_shopping_data_year_2021.csv", index=False)
data_2022.to_csv("customer_shopping_data_year_2022.csv", index=False)
data_2023.to_csv("customer_shopping_data_year_2023.csv", index=False)

# a for-loop to analyze the DataFrames for the years 2021, 2022 and 2023
# first, creating a list, then start the loop
list_dataframes = [data_2021, data_2022, data_2023]
current_year = 2021
for df in list_dataframes:
    data_year = df

    print("The statistical analysis for the year "+ str(current_year) + " beginns:")
    print()

    # looking for correlations
    print_spaced(data_year.corr(numeric_only=True))

    # creating a DataFrame with statistical analysis for the entire dataset
    # output of the statistical analysis to illustrate which evaluation is carried out
    stats_entire = stats_evaluation.stats(data_year)
    print("The statistical analysis for the entire dataset:")
    stats_entire["shopping_mall"] = "Entire Dataset"
    stats_entire["year"] = current_year
    print_spaced(stats_entire)

    # each shopping center name is added to a list
    mall_list = sorted(data_year["shopping_mall"].unique())

    # a for-loop to execute the statistical analysis for each shopping mall
    # the same evaluations are carried out as for the entire data set
    # an output for each shopping mall is omitted due to confusion
    result = []
    for name in mall_list:
        mall_df = data_year[data_year["shopping_mall"] == name]
        mall_df = stats_evaluation.stats(mall_df)
        mall_df["shopping_mall"] = name
        mall_df["year"] = current_year
        result.append(mall_df)

    mall_summary = pd.concat(result)
    data_combined = pd.concat([stats_entire,mall_summary])
    data_combined.to_excel("summary_stats_customer_shopping_data_year_"+str(current_year)+".xlsx")

    current_year = current_year + 1

print(f"{'The statistical analysis was saved in Excel sheets and is ready for further evaluations':*<100}")
