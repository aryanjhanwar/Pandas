import pandas as pd

ipl_df = pd.read_csv("2_Dataframes_pandas/datasets/ipl-matches.csv")
print(ipl_df)

# filtering the dataframe 

#? filter the dataframe for matches played in 2017
# print("\nFiltering the dataframe for matches played in 2017:")
# print(ipl_df[ipl_df["Season"] == "2017"]) # filtering the dataframe for matches played in 2017, returns a dataframe

#? find all the final winners
# print(ipl_df[ipl_df["MatchNumber"] == "Final"][["Season" , "Team1" , "Team2" , "WinningTeam"]]) # filtering the dataframe for matches played in 2017, returns a dataframe

#? how many super over finishes have occured
print(ipl_df[ipl_df["SuperOver"] == 'Y'].shape) # len() is also accurate

#? how many matches has csk won in kolkata
print(ipl_df[(ipl_df["City"] == "Kolkata") & (ipl_df["WinningTeam"] == "Chennai Super Kings")].shape[0])

#? toss winner is match winner in percentage
# no_of_winning_teams_toss_winner = ipl_df[ipl_df["TossWinner"] == ipl_df['WinningTeam']][["TossWinner" , "WinningTeam"]].shape[0]
# print(no_of_winning_teams_toss_winner/ipl_df.shape[0] * 100) # filtering the dataframe for matches where toss winner is also the match winner, returns a series of winning teams

movies_df = pd.read_csv("2_Dataframes_pandas/datasets/movies.csv")
print(movies_df)

#? Action movies with rating higher than 7.5
print(movies_df[(movies_df["genres"].str.contains("Action")) & (movies_df["imdb_rating"] > 7.5)][["title_x" , "genres" , "imdb_rating"]]) # filtering the dataframe for action movies with rating higher than 7.5, returns a dataframe

print(movies_df[(movies_df["imdb_rating"] > 8) & (movies_df["imdb_votes"] > 10000)][["title_x" , "imdb_votes" , "imdb_rating"]].shape)