import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl = pd.read_csv("2_Dataframes_pandas/datasets/ipl-matches.csv")
print(ipl)

# value_counts() method
print(ipl["WinningTeam"].value_counts())

#? find which player has won most potm -> in finals and qualifiers
print(ipl[(~ipl["MatchNumber"].str.isdigit())]["Player_of_Match"].value_counts())


# Toss decision plot
# ipl['TossDecision'].value_counts().plot(kind='pie')
# plt.show()

print(ipl[ipl["TossDecision"] == "field"].shape[0] / ipl.shape[0] * 100)

# how many matches each team has played
print((ipl["Team2"].value_counts() + ipl["Team1"].value_counts()).sort_values(ascending=False))

# sort_values() method
print(ipl.sort_values("Date" , ascending=True).head(10))


students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

# sort_values() with null values
print(students.sort_values("name" , na_position= "first" , ascending=True))
print(students.sort_values("name" , na_position= "last" , ascending=True))

# sort_values() with multiple columns
movies_dataframe = pd.read_csv("2_Dataframes_pandas/datasets/movies.csv")
print(movies_dataframe)

print(movies_dataframe.sort_values(["year_of_release" , "title_x"] , ascending=[True , False])[["title_x" , "year_of_release"]])

# rank() method
batsmanipl = pd.read_csv("2_Dataframes_pandas/datasets/batsman_runs_ipl.csv")
print(batsmanipl)

batsmanipl["rank"] = batsmanipl["batsman_run"].rank(ascending=False)
print(batsmanipl)

print(batsmanipl.sort_values("rank").head(20))

# sort_index() in dataframe
print(movies_dataframe.sort_index(ascending=False).head(10))

# sort_index() with multiple levels of index
print(batsmanipl.set_index("batter"))

# reset_index() method in dataframe
print(batsmanipl.set_index("batter").reset_index())

# replace index with reset_index() method in dataframe
print(batsmanipl.reset_index().set_index("rank"))

# rename method in dataframe
print(movies_dataframe.rename(columns={"title_x":"movie_title" , "year_of_release":"release_year"}).head(10))
# rename index in dataframe
print(movies_dataframe.rename(index={0:"first_movie" , 1:"second_movie"}).head(10))

# unique() method in dataframe
#! print(movies_dataframe["genre"].unique())
# nunique() method in dataframe
#! print(movies_dataframe["genre"].nunique())
# unique() method counts the number of unique values in a column and returns an array of those unique values, 
# unique involves the nan values as well, while nunique() method does not count the nan values and only counts the unique non-null values in a column.
# while nunique() method counts the number of unique values in a column and returns that count as an integer. 


# isnull() method in dataframe -> it is used to check for missing values in a dataframe. It returns a boolean dataframe of the same shape as the original dataframe, where each cell contains True if the corresponding value in the original dataframe is null (missing) and False otherwise.
print(movies_dataframe.isnull().sum())

# notnull() method in dataframe -> it is used to check for non-missing values in a dataframe. It returns a boolean dataframe of the same shape as the original dataframe, where each cell contains True if the corresponding value in the original dataframe is not null (not missing) and False otherwise.
print(movies_dataframe.notnull().sum())

# hasna() method in dataframe -> it is used to check if there are any missing values in a dataframe. It returns a boolean value, True if there are any missing values in the dataframe and False otherwise.
print(movies_dataframe["title_x"].hasnans)


print(students)
# dropna() method in dataframe -> it is used to remove missing values from a dataframe. It can be used to drop rows or columns that contain missing values, depending on the specified parameters.
print(students.dropna()) # drop rows even if there is a single missing value in that row
print(students.dropna(how="all")) # drop rows only if all values in that

print(students.dropna(subset=["name" , "college"])) # drop rows if there is a missing value in either name or college column


# fillna() method in dataframe -> it is used to fill missing values in a dataframe with a specified value or method. It can be used to fill missing values with a constant value, the mean, median, or mode of the column, or by using forward or backward filling methods.

print(students["name"].fillna("unknown")) # fill missing values in name column with "unknown"

print(students["cgpa"].fillna(students["cgpa"].mean())) # fill missing values in cgpa column with mean of cgpa column
print(students["name"].ffill()) # fill missing values in name column with forward fill method
print(students["branch"].bfill()) # fill missing values in branch column with backward fill method

marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

# drop_duplicates() method in dataframe -> it is used to remove duplicate rows from a dataframe. It can be used to drop duplicate rows based on all columns or a subset of columns, depending on the specified parameters.
print(marks)
print(marks.drop_duplicates()) # drop duplicate rows based on all columns

# duplicated() method in dataframe -> it is used to identify duplicate rows in a dataframe. It returns a boolean series of the same length as the original dataframe, where each value is True if the corresponding row is a duplicate and False otherwise.
print(marks.duplicated()) # identify duplicate rows based on all columns

# drop() method in dataframe -> it is used to remove specified rows or columns from a dataframe. It can be used to drop rows or columns based on their labels or index positions, depending on the specified parameters.
print(marks.drop(columns=["package"])) # drop the package column from the dataframe
print(marks.drop(index=[0,1])) # drop the first and second row from the dataframe



points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)

print(points_df)

# apply() method in dataframe -> it is used to apply a function along an axis of the dataframe (either rows or columns). It can be used to apply a function to each element, row, or column of the dataframe, depending on the specified parameters.

def euclidean_distance(row):
    pt_A = row["1st point"]
    pt_B = row["2nd point"]

    return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5

points_df["distance"] = points_df.apply(euclidean_distance , axis=1) # axis=1 (for rows)
print(points_df)

