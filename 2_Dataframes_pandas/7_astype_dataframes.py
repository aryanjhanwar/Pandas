import pandas as pd

# astype method in dataframe
movies_df = pd.read_csv("2_Dataframes_pandas/datasets/movies.csv")
print(movies_df.dtypes) # data types of each column in the dataframe


# converting the data type of a column in the dataframe
movies_df["imdb_rating"] = movies_df["imdb_rating"].astype("float") # converting the data type of a column in the dataframe, returns a dataframe
print("\nData types of each column in the dataframe after converting the data type of a column:")
print(movies_df.dtypes) # data types of each column in the dataframe after converting the data type of a column
