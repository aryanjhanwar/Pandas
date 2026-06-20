import numpy as np
import pandas as pd

movies_dataframe = pd.read_csv("2_Dataframes_pandas/datasets/movies.csv")
print(movies_dataframe)

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)


# selecting a single column from the dataframe
print("\nSelecting a single column from the dataframe:")
print(movies_dataframe["title_x"]) # selecting a single column from the dataframe, returns a series

# selecting multiple columns from the dataframe
print("\nSelecting multiple columns from the dataframe:")
print(movies_dataframe[["title_x" , "genres"]]) # selecting multiple columns from the dataframe, returns a dataframe


# loc and iloc methods in dataframe
# loc method is used to select rows and columns by label, 


# iloc method is used to select rows and columns by index,

print("\nSelecting rows and columns using loc method:")
print(movies_dataframe.loc[0]) # selecting a single row from the dataframe using loc method, returns a series
print(movies_dataframe.loc[0:5]) # selecting multiple rows from the dataframe using loc
print(movies_dataframe.loc[: ,["title_x" , "genres"]]) # selecting multiple rows and a single column from the dataframe using loc
print(movies_dataframe.loc[: , "title_x" : "genres"]) # selecting multiple rows and a single column from the dataframe using loc


print("\nSelecting rows and columns using iloc method:")
print(movies_dataframe.iloc[0]) # selecting a single row from the dataframe using iloc
print(movies_dataframe.iloc[0:5]) # selecting multiple rows from the dataframe using iloc
print(movies_dataframe.iloc[0:5 , 0:3]) # selecting multiple rows and columns from the dataframe using iloc
#! error print(movies_dataframe.iloc[: , "title_x" : "genres"]) # selecting multiple rows and a single column from the dataframe using loc

