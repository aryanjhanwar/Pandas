import numpy as np
import pandas as pd

# Create a Series from a dictionary
marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "History": 82,
    "Geography": 88
}

marks_series = pd.Series(marks , name="My Marks")
print("\nSeries from a dictionary:")
print(marks_series)

# Attributes of a Series
print("\nAttributes of the Series:")

# Index: The labels of the Series
print("Index:", marks_series.index)

# Values: The data values of the Series
print("\nValues:", marks_series.values)

# Data Type: The data type of the values in the Series
print("\nData Type:", marks_series.dtype)

# Name: The name of the Series
print("\nName:", marks_series.name)

# Is Unique: Whether the index labels are unique
print("\nis Unique:", marks_series.is_unique)

