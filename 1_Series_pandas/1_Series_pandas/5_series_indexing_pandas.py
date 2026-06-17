import numpy as np
import pandas as pd

series_subs = pd.read_csv("1_Series_pandas/datasets/subs.csv").squeeze("columns")
print("\nSeries for Subs:")
print(series_subs)

series_vk = pd.read_csv("1_Series_pandas/datasets/kohli_ipl.csv" , index_col="match_no").squeeze("columns")
print("\nSeries for Kohli IPL runs:")
print(series_vk)

series_bollywood = pd.read_csv("1_Series_pandas/datasets/bollywood.csv" , index_col = "movie").squeeze("columns")
print("\nSeries for Bollywood collections:")
print(series_bollywood)

x = pd.Series([12 , 13 , 14 , 35 , 46 , 57 , 58 , 79 , 9])

# indexing in Series
print("\nIndexing in Series:")
print("Element at index 0:", x[0])
print("Element at index 3:", x[3])

# negative indexing in Series does not work like in lists, it will raise an error
print("\nNegative Indexing in Series:")
try:
    print("Element at index -1 (last element):", x[-1])
except Exception as e:
    print("Error:", e)

# Indexing doesnt work in series like in lists, it works based on the index labels. 
# If the index is default (0, 1, 2, ...), then it will work like list indexing. But if the index is custom (like in series_bollywood), then we need to use the index labels for indexing.
print("\nIndexing in Series with custom index:")
print(series_bollywood["Evening Shadows"])

print(series_subs[0]) # works because index is default
try:
    print(series_subs[-1]) # raises error because negative indexing does not work in Series
except Exception as e:
    print("Error:", e)

# slicing in Series works based on index labels, 
# not based on position like in lists. 
# So we need to use the index labels for slicing.
print(series_vk[::2]) # works because index is default
try:
    print(series_vk[-3:-1]) # it works because slicing with negative indices works in Series, 
    # it will slice based on position from the end of the Series.
except Exception as e:
    print("Error:", e)

# fancy indexing in Series also works based on index labels, not based on position like in lists.
print(series_vk[[1 , 2 ,5 , 7]]) # works because we are using index labels for fancy indexing


marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "History": 82,
    "Geography": 88
}

marks_series = pd.Series(marks , name="My Marks")
print("\nOriginal Series:")
print(marks_series)

# updating the value of a specific index label
marks_series["Maths"] = 95
print("\nUpdated Series:")
print(marks_series)

marks_series["Art"] = 80 # this will add a new index label "Art" with value 80, 
# it will not raise an error

print(marks_series)


