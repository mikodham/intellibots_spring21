import pandas as pd

df = pd.DataFrame()


path = "./Dataset/reddit.csv"
df = pd.read_csv(path,usecols=[1,2]) 

df_negatives = df[df['class'].isin(['non-suicide'])]
df_negatives.reset_index(drop=True,inplace=True)
#print(df_negatives.head(100))

df_positives = df[df['class'].isin(['suicide'])]
df_positives.reset_index(drop=True,inplace=True)
#print(df_positives.head(100))

#print(len(df_negatives.index),len(df_positives.index))

