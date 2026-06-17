import pandas as pd

marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "History": 82,
    "Geography": 88
}

marks_series = pd.Series(marks , name="My Marks")
series_bollywood = pd.read_csv("1_Series_pandas/datasets/bollywood.csv" , index_col = "movie").squeeze("columns")
print(series_bollywood)

# membership operator in series
print("Membership operator in Series:")
print("3 Idiots" in series_bollywood.index) # True
print("Dangal" in series_bollywood) # False
print("Alia Bhatt" in series_bollywood.values) # True


# looping in series
print("\nLooping in Series:")
for movie in series_bollywood.index:
    print(movie)

# airthmetic operations on Series
print("\nArithmetic operations on the Series:")
# addition
print(marks_series + 100) # adds 100 to each value in the Series
# subtraction
print(100 - marks_series) # subtracts 100 from each value in the Series


series_vk = pd.read_csv("1_Series_pandas/datasets/kohli_ipl.csv" , index_col="match_no").squeeze("columns")

# Boolean indexing in series
print(len(series_vk[series_vk >= 50])) # length of the Series
print(series_vk[series_vk >= 50].size) # size of the Series