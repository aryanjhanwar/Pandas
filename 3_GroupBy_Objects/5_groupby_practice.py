import pandas as pd

deliveries = pd.read_csv("3_GroupBy_Objects/datasets/deliveries.csv")
print(deliveries)

batsmangroup = deliveries.groupby("batsman")
# find the top 10 batsman in terms of runs
print(batsmangroup["batsman_runs"].sum().sort_values(ascending=False))

# find the batsman with max no of sixes
six_df = deliveries[deliveries["batsman_runs"] == 6]
print(six_df)

batsmanG = six_df.groupby("batsman")["batsman"].count().sort_values(ascending=False).head(10)
print(batsmanG)

# find batsman with most number of 4's and 6's in last 5 overs


last5o_4_6 = deliveries[(deliveries["over"] > 15) & ((deliveries["batsman_runs"] == 4) | (deliveries["batsman_runs"] == 6))]
print(last5o_4_6)

batsmanG = last5o_4_6.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(10)
print(batsmanG)


# find V Kohli's record against all teams
temp_df = deliveries[deliveries["batsman"] == "V Kohli"]
teams_group = temp_df.groupby("bowling_team")["batsman_runs"].sum()
print(teams_group)

# Create a function that can return the highest score of any batsman
def highest_score(batsman):
    temp_df = deliveries[deliveries["batsman"] == batsman]
    match_group = temp_df.groupby("match_id")["batsman_runs"].sum().sort_values(ascending=False).head(1).values[0]
    return match_group

print(highest_score("CH Gayle"))
