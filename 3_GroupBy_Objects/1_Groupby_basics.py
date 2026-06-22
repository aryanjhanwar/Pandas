import numpy as np
import pandas as pd

movies = pd.read_csv("3_GroupBy_Objects/datasets/imdb-top-1000.csv")
print(movies)

# Group By -> groupby() method in dataframe -> it is used to group the data in a dataframe based on one or more columns. It returns a GroupBy object that can be used to perform various operations on the grouped data, such as aggregation, transformation, and filtering.
print("Group By Object : ")
grouped_data = movies.groupby('Genre') # doesnt display grouped data
print(grouped_data)

# groupby() method with aggregation functions
print("Group By Object with Aggregation Functions : ")
print(grouped_data.sum()) # sum of all numeric columns for each genre


print(grouped_data.sum(numeric_only=True)) # gives the sum of only numeric columns for each genre

print(type(grouped_data.sum())) # type of the result is a dataframe
print(grouped_data["IMDB_Rating"].mean()) # mean rating for each genre

# Q: find the top 3 genres by gross earning
# print(grouped_data.sum().sort_values("Gross" , ascending=False).head(3)[["Genre" , "Gross"]]) # wrong
print(grouped_data.sum().sort_values("Gross" , ascending=False).head(3)[["Gross" , "Metascore"]]) # right
print(grouped_data["Gross"].sum().sort_values(ascending=False).head(3)) # more efficient way 

# find the genre with highest avg IMDB rating
print(grouped_data["IMDB_Rating"].mean().sort_values(ascending=False).head(1))

# find director with most popularity
grouped_dir_data = movies.groupby("Director")
print(grouped_dir_data["No_of_Votes"].sum().sort_values(ascending=False).head(1))


# find the highest rated movie of each genre
grouped_data = movies.groupby('Genre')

data = movies[["Series_Title" , "IMDB_Rating" , "Genre"]]
print(data.sort_values("IMDB_Rating" , ascending=False).groupby("Genre").max())

print(
    movies.loc[
        movies.groupby("Genre")["IMDB_Rating"].idxmax(),
        ["Genre", "Series_Title", "IMDB_Rating"]
    ]
)

# find the no of movies done by each actor
print(movies["Star1"].value_counts())

# by using group by 
print(movies.groupby("Star1" ).count().sort_values("Series_Title" , ascending=False ))