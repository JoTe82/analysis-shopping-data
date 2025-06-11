"""
Module for statistical evaluation: customer_shopping_data.csv

Data Source: The dataset used, "Customer Shopping Dataset – Retail Sales Data",  
was obtained from the platform Kaggle.com and is published under the  
Creative Commons CC0 1.0 Universal (Public Domain Dedication) license.  
The authors have waived all copyright and related rights to this data.

License details: https://creativecommons.org/publicdomain/zero/1.0/deed.en
"""

# statistics, numpy, pandas and matplotlib import
import statistics
import pandas as pd

# a function for statistical analysis
def stats(dataset):
    # statistical analysis of all columns with quantitative values
    stat = pd.DataFrame(dataset.describe())

    # calculation of all missing statistical values - median, mode u span
    list_columns = dataset.select_dtypes(include=[int,float]).columns.to_list() 
    list_median = []
    list_mode = []
    list_span = []

    # a for-loop to determine the missing values
    # the results are written to a list
    for i in list_columns:
        median = statistics.median(dataset[i])
        mode = statistics.mode(dataset[i])
        span = max(dataset[i]) - min(dataset[i])
        list_median.append(median)
        list_mode.append(mode)
        list_span.append(span)

    # each list will be transform into a Series 
    # setting an index for the Series
    index_columns_series = list_columns
    median = pd.Series(list_median, index=index_columns_series)
    mode = pd.Series(list_mode, index=index_columns_series)
    span = pd.Series(list_span, index=index_columns_series)

    # creating a new DataFrame from the Series
    # setting an Index for the rows
    index_rows_df = ["median","mode","span"]
    stat_two = pd.DataFrame([median,mode,span], index=index_rows_df)

    # connect both DataFrame with concat
    stat = pd.concat([stat,stat_two])

    return stat