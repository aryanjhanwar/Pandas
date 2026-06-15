import pandas as pd

df_subs = pd.read_csv("1_Series_pandas/datasets/subs.csv")
series_subs = df_subs.squeeze("columns")

print(type(series_subs))
print(series_subs)


df_vk = pd.read_csv("1_Series_pandas/datasets/kohli_ipl.csv" , index_col="match_no")
series_vk = df_vk.squeeze("columns")
print(series_vk)


df_bollywood = pd.read_csv("1_Series_pandas/datasets/bollywood.csv" , index_col = "movie")
series_bollywood = df_bollywood.squeeze("columns")

print(series_bollywood)
