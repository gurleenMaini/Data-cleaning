import pandas as pd 

df = pd.read_csv("starInfo_sorted1.csv")
del df["Luminosity"]
df.to_csv("final.csv")

print(df.shape)
print(list(df))