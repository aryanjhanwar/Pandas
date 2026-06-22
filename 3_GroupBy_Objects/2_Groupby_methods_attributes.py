import pandas as pd

movies = pd.read_csv("3_GroupBy_Objects/datasets/imdb-top-1000.csv")
print(movies)

# len() in groupby object gives the number of groups
grouped_data = movies.groupby('Genre')
print(len(grouped_data)) # number of unique genres
print(grouped_data.nunique()) # number of unique genres

# size attribute gives the size of each group and no of rows in each group
print(grouped_data.size()) # number of movies in each genre

# value_counts() method gives the count of each unique value in the groupby object
# value_counts() gives output in sorted order whereas size() gives output in the order of the groups
print(movies["Genre"].value_counts()) # count of each genre in the dataset


# first/last/nth gives the first/last row of each group
print(grouped_data.first()) # first movie of each genre
print(grouped_data.last()) # last movie of each genre
print(grouped_data.nth(2)) # 3rd movie of each genre (0-based index)


# get_group() method gives the group of a specific value in the groupby object
print(grouped_data.get_group("Horror")) # all movies in the Horror genre


# groups attribute gives the groups in the groupby object
print(grouped_data.groups) # groups in the groupby object in the form of a dictionary with group names as keys and indices of rows in each group as values

# describe() method gives the summary statistics of each group
print(grouped_data.describe()) # summary statistics of each genre

# sample() method gives a random sample of rows from each group
# print(grouped_data.sample(n=2)) # random sample of 2 movies from each genre

# agg() method allows us to apply multiple aggregation functions to the grouped data
agg_result = grouped_data.agg({
    "IMDB_Rating": ["mean", "max", "min"],
    "Gross": ["sum", "mean"],
    "No_of_Votes": ["sum", "mean"],
    "Metascore": ["mean", "max", "min"]
})

print(agg_result)