import pandas as pd

df = pd.DataFrame()

path = "./Dataset/reddit.csv"
df = pd.read_csv(path,usecols=[1,2]) # ignore first column

df_negatives = df[df['class'].isin(['non-suicide'])]
df_negatives_mini = df_negatives.sample(n=10000) 

df_positives = df[df['class'].isin(['suicide'])]
df_positives_mini = df_positives.sample(n=10000)

df = pd.concat([df_negatives_mini,df_positives_mini],ignore_index=True)

df.to_csv('./Dataset/reddit_mini.csv')


