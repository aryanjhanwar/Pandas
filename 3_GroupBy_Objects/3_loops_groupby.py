import numpy as np
import pandas as pd

movies = pd.read_csv("3_GroupBy_Objects/datasets/imdb-top-1000.csv")
print(movies)

# loops with groupby objects
grouped_data = movies.groupby('Genre')


# iterating through groupby object  
# for genre, group in grouped_data:
#     print(f"Genre: {genre}")
#     print(group[["Series_Title", "IMDB_Rating"]].head(5)) # print first 5 movies of each genre with their ratings

group_horror = grouped_data.get_group('Horror')
mask1 = grouped_data.get_group('Horror')["IMDB_Rating"].max() == group_horror["IMDB_Rating"]
print(group_horror[mask1])
print(mask1)

highest_rating_df = pd.DataFrame(columns=["Series_Title", "IMDB_Rating"])


# find the highest rated movie of each genre
for genre, group in grouped_data:
    print(f"Genre: {genre}", end="  ")

    highest_movie = (
        group[group["IMDB_Rating"] == group["IMDB_Rating"].max()]
        .head(1)[["Series_Title", "IMDB_Rating"]]
    )

    highest_movie.index = [genre]

    highest_rating_df = pd.concat([
        highest_rating_df,
        highest_movie
    ])
print(highest_rating_df)

# find number of movies starting with A for each group
data = []

for genre, group in grouped_data:
    count = group["Series_Title"].str.startswith("A").sum()

    data.append({
        "Genre": genre,
        "Start_with_A": count
    })

starts_with_A = pd.DataFrame(data)
starts_with_A.set_index("Genre", inplace=True)
print(starts_with_A.sort_values("Start_with_A", ascending=False))


# by using apply() method
def foo(group):
    return group["Series_Title"].str.startswith("A").sum()

print(grouped_data.apply(foo).sort_values(ascending=False))

# find ranking of each movie in the group according to IMDB score

def rank_movies(group) : 
    group["genre_rank"] = group["IMDB_Rating"].rank(ascending=False)
    return group

print(grouped_data.apply(rank_movies))



# find normalized IMDB rating group wise
def normalize(group):
    Rating = group["IMDB_Rating"]
    group["norm_rating"] = (Rating - Rating.min()) / (Rating.max() - Rating.min())
    return group

print(grouped_data.apply(normalize))