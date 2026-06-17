import numpy as np
import pandas as pd


df_subs = pd.read_csv("1_Series_pandas/datasets/subs.csv")
series_subs = df_subs.squeeze("columns")

print(type(series_subs))


df_vk = pd.read_csv("1_Series_pandas/datasets/kohli_ipl.csv" , index_col="match_no")
series_vk = df_vk.squeeze("columns")

df_bollywood = pd.read_csv("1_Series_pandas/datasets/bollywood.csv" , index_col = "movie")
series_bollywood = df_bollywood.squeeze("columns")




# head -> first n rows of the Series (default n=5)
print("\nHead of the Series:")
print(series_bollywood.head())
print(series_bollywood.head(3))

# tail -> last n rows of the Series (default n=5)
print("\nTail of the Series:")
print(series_bollywood.tail())
print(series_bollywood.tail(10))

# sample -> random n rows of the Series (default n=1)
print("\nRandom Sample from the Series:")
print(series_bollywood.sample())
print(series_bollywood.sample(3))

# value_counts -> count of unique values in the Series
print("\nValue Counts of the Series:")
print(series_bollywood.value_counts()) 

# sort_values -> sort the Series by values
print("\nSeries sorted by values:")
print(series_bollywood.sort_values()) # ascending order by default
print(series_bollywood.sort_values(ascending=False )) # descending order
# for permanent values sorting, we can use inplace=True
#? series_bollywood.sort_values(inplace=True)

# sort_index -> sort the Series by index
print("\nSeries sorted by index:")
print(series_bollywood.sort_index()) # ascending order by default
print(series_bollywood.sort_index(ascending=False)) # descending order
# for permanent index sorting, we can use inplace=True
#? series_bollywood.sort_index(inplace=True)


# mathematical operations on Series
print("\nMathematical operations on the Series:")

# count -> count of non-null values in the Series
print("Count of non-null values:", series_bollywood.count())

# statistical measures in pandas
# mean -> average of the values in the Series
print("Mean:", series_subs.mean())
# median -> middle value of the sorted Series
print("Median:", series_subs.median())
# mode -> most frequent value(s) in the Series
print("Mode:", series_subs.mode())
# standard deviation -> measure of the spread of the values in the Series
print("Standard Deviation:", series_subs.std())
# variance -> measure of the variability of the values in the Series
print("Variance:", series_subs.var())

# minimum and maximum values in the Series
print("Minimum value:", series_subs.min())
print("Maximum value:", series_subs.max())


# describe -> summary statistics of the Series
print("\nSummary statistics of the Series:")
print(series_subs.describe())

# basic methods for Series
print("\nBasic methods for the Series:")
# len/type/dir/sorted/max/min
print(len(series_subs))
print(type(series_subs))
print(dir(series_subs))
print(sorted(series_subs))
print(min(series_subs))
print(max(series_subs))


marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "History": 82,
    "Geography": 88
}

marks_series = pd.Series(marks , name="My Marks")
# type conversion
print("\nType conversion of the Series:")
print(list(marks_series)) # convert Series to list
print(dict(marks_series)) # convert Series to dictionary
print(marks_series.to_frame()) # convert Series to DataFrame


