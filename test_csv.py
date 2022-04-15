import pandas as pd

df = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL.csv')
print(df.head())
df.info()
