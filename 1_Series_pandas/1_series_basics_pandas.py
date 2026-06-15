import numpy as np
import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]

series = pd.Series(data)
print("Series from a list:")
print(series)

# custom index
custom_index = ["a", "b", "c", "d", "e"]
series_custom = pd.Series(data , index = custom_index)
print("\nSeries with custom index:")
print(series_custom)

# Create a Series with a name
series_custom2 = pd.Series(data , index = custom_index , name = "My Series")
print("\nSeries with extended custom index:")
print(series_custom2)


# Create a Series from a dictionary
marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "History": 82,
    "Geography": 88
}

series_from_dict = pd.Series(marks , name="My Marks")
print("\nSeries from a dictionary:")
print(series_from_dict)

