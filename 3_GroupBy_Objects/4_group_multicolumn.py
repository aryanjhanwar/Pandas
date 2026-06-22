import pandas as pd

movies = pd.read_csv("3_GroupBy_Objects/datasets/imdb-top-1000.csv")
print(movies)

# groupby() method with multiple columns
director_actor_group = movies.groupby(["Director" , "Star1"])

print(director_actor_group.size().sort_values(ascending=False))

# find the most earning actor->director combo
# print(director_actor_group[director_actor_group["Gross"].sum().max() == director_actor_group["Gross"].sum()])

gross_sum = director_actor_group["Gross"].sum()
print(type(gross_sum))
print(gross_sum[gross_sum == gross_sum.max()])

# find the best(in-terms of metascore(avg)) actor->genre combo
actor_genre_group = movies.groupby(["Star1" , "Genre"])
print(actor_genre_group["Metascore"].mean().sort_values(ascending=False).head(10))


# aggerate