import pandas as pd

# df = pd.read_csv("df_noreview.csv")
# # print(df.head())
# print(df.info())

df = pd.read_json("bd_allresults.json")
print(df.head())
print(df.shape)
print(df.info())