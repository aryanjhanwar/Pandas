import pandas as pd

ipl_dataframe = pd.read_csv("2_Dataframes_pandas/datasets/ipl-matches.csv")
print(ipl_dataframe)

# shape attribute in dataframe
print("\nShape of the dataframe:")
print(ipl_dataframe.shape) # (number of rows , number of columns)

# dtypes attribute in dataframe
print("\nData types of each column:")
print(ipl_dataframe.dtypes) # data types of each column in the dataframe

# index attribute in dataframe
print("\nIndex of the dataframe:")
print(ipl_dataframe.index) # no. of index of the dataframe

# columns attribute in dataframe
print("\nColumns of the dataframe:")
print(ipl_dataframe.columns) # columns of the dataframe

# values attribute in dataframe
print("\nValues of the dataframe:")
print(ipl_dataframe.values) # values of the dataframe in 2D array format

# head and tail attributes in dataframe
print("\nFirst 5 rows of the dataframe:")
print(ipl_dataframe.head()) # first 5 rows of the dataframe
print("\nLast 5 rows of the dataframe:")
print(ipl_dataframe.tail()) # last 5 rows of the dataframe


# sample attribute in dataframe
print("\nRandom sample of 5 rows from the dataframe:")
print(ipl_dataframe.sample()) # random sample of 1 row from the dataframe

# info attribute in dataframe
print("\nInformation about the dataframe:")
print(ipl_dataframe.info()) # information about the dataframe such as number of non-null values,

# describe attribute in dataframe
print("\nStatistical summary of the dataframe:")
print(ipl_dataframe.describe()) # statistical summary of the dataframe such as mean, std, min, max, etc. for numerical columns

# isnull attribute in dataframe
print("\nCheck for null values in the dataframe:")
print(ipl_dataframe.isnull()) # check for null values in the dataframe, returns a dataframe of boolean values
print(ipl_dataframe.isnull().sum()) # count of null values in each column of the dataframe


# rename 
student_list_dataframe = pd.DataFrame({
    "iq" : [100 , 90 , 120 ,80 , 0 , 0],
    "marks" : [80 , 70 , 100 , 50 , 0 , 0],
    "package" : [10 , 7 , 14 ,2 , 0 , 0]
})

# duplicated attribute in dataframe
print("\nCheck for duplicate rows in the dataframe:")
print(student_list_dataframe.duplicated()) # check for duplicate rows in the dataframe, returns a series of boolean values
print(student_list_dataframe.duplicated().sum()) # count of duplicate rows in the dataframe


# rename attribute in dataframe
print("\nRename columns of the dataframe:")
student_list_dataframe.rename(columns={"iq" : "IQ" , "marks" : "Marks" , "package" : "Package"} , inplace=True)
print(student_list_dataframe)

# mathematical operations on dataframe
print("Sum of IQ and Marks columns:")
print(student_list_dataframe.sum()) # sum of each column in the dataframe default axis=0
print(student_list_dataframe.sum(axis=1)) # sum of each row in the dataframe axis=1

# mean/median/mode/std/var/min/max attributes in dataframe
# all works in axis =0 by default, for axis=1 we need to specify it in the function

# mean -> average of the values in the Series
print("Mean:\n", student_list_dataframe.mean())
# median -> middle value of the sorted Series
print("Median:\n", student_list_dataframe.median())
# mode -> most frequent value(s) in the Series
print("Mode:\n", student_list_dataframe.mode())
# standard deviation -> measure of the spread of the values in the Series
print("Standard Deviation:\n", student_list_dataframe.std())
# variance -> measure of the variability of the values in the Series
print("Variance:\n", student_list_dataframe.var())

# minimum and maximum values in the Series
print("Minimum value:\n", student_list_dataframe.min())
print("Maximum value:\n", student_list_dataframe.max())

