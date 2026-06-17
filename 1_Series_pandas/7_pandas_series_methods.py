import pandas as pd
import numpy as np

df_vk = pd.read_csv("1_Series_pandas/datasets/kohli_ipl.csv" , index_col="match_no")
series_vk = df_vk.squeeze("columns")

# astype method in Series

print("\nData type of the Series before converting:")
print(series_vk.dtypes) # data type of the Series before converting
# converting the data type of the Series
series_vk = series_vk.astype("int16") # converting the data type of the Series, returns a Series
print("\nData type of the Series after converting:")
print(series_vk.dtypes) # data type of the Series after converting

# between method in Series
print("\nValues between 50 and 100 in the Series:")
print(series_vk[series_vk.between(50 , 100)]) # values between 50 and 100 in the Series, returns a Series of boolean values


# clip method in Series
print("\nSeries after clipping values between 50 and 100:")
print(series_vk.clip(40 , 80).head(100)) # Series after clipping values between 40 and 80

# drop_duplicates method in Series
series_dup = pd.Series([1,2,3,4,5,5,6,7,8,9,10])
print("\nSeries after dropping duplicate values:")
print(series_dup.drop_duplicates()) # Series after dropping duplicate values, returns a Series

print("\nSeries after dropping duplicate values and keeping the last occurrence:")
print(series_dup.drop_duplicates(keep="last")) # Series after dropping duplicate values and keeping the last occurrence, returns a Series

print(series_dup.duplicated().sum()) # check for duplicate values in the Series, returns a Series of boolean values

temp_series = pd.Series([1,2,np.nan,4,np.nan,5,6,np.nan,8,9,10])

# size method in Series -> null + non-null values in the Series
print("\nSize of the Series:")
print(temp_series.size) # size of the Series, returns an integer
# count method in Series -> non-null values in the Series
print("\nCount of non-null values in the Series:")
print(temp_series.count()) # count of non-null values in the Series, returns an integer

print("\nCheck for null values in the Series:")
print(temp_series.isnull().sum()) # check for null values in the Series, returns an integer


# dropna method in Series -> drop null values from the Series
print("\nSeries after dropping null values:")
print(temp_series.dropna()) # Series after dropping null values, returns a Series

# fillna method in Series -> fill null values in the Series with a specified value
print("\nSeries after filling null values with 0:")
print(temp_series.fillna(0)) # Series after filling null values with 0, returns a Series

# isin method in Series -> check if values in the Series are present in a specified list of values
print("\nCheck if values in the Series are present in the list [1,2,3]:")
print(temp_series.isin([1,2,3])) # check if values in the Series


# apply method in Series -> apply a function to each value in the Series
print(series_vk.mean()) # mean of the Series
print(series_vk.apply(lambda x : "good play" if x > series_vk.mean() else "bad play"))
print(series_vk)

# copy method in Series -> create a copy of the Series
print("\nCopy of the Series:")
series_copy = series_vk.copy() # create a copy of the Series, returns a Series
print(series_copy)
series_copy[1] = 100 # modifying the copy of the Series
print("\nModified copy of the Series:")
print(series_copy) # modified copy of the Series
print("\nOriginal Series after modifying the copy:")
print(series_vk) # original Series after modifying the copy, remains unchanged