import pandas as pd

master_df = pd.DataFrame()

file_urls = [
    "https://zenodo.org/record/4543776/files/Redditors_and_posts_batch_1.xlsx", # 757 posts
    "https://zenodo.org/record/4543776/files/Redditors_and_posts_batch_2.xlsx", # 934 posts
    "https://zenodo.org/record/4543776/files/Redditors_and_posts_batch_3.xlsx", # 837 posts
    "https://zenodo.org/record/4543776/files/Redditors_and_posts_batch_4.xlsx", # 983 posts 
    "https://zenodo.org/record/4543776/files/Redditors_and_posts_batch_5.xlsx", # 761 posts
]

for file_url in file_urls:

    dfs = pd.read_excel(file_url,sheet_name=None,usecols="A:B") # 1 dataframe for each sheet within an excel file
    df = pd.concat(dfs,ignore_index=True) # merging the dataframes for each sheet
    master_df = pd.concat([master_df,df],ignore_index=True) # merging the dataframes for each file

master_df.to_csv(r'master_data.csv',sep='|',index=False)