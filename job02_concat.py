import pandas as pd
import glob
data_paths = glob.glob('./crawling_data/*')
print(data_paths)
df = pd.DataFrame()
for path in data_paths[1:]:
    df_temp = pd.read_csv(path)
    df_temp.columns = ['title', 'reviews','scores','genres']
    df = pd.concat([df, df_temp], ignore_index=True,
              axis='rows')
df.info()
df.to_csv('./crawling_data/datasets/Game_reviews_ALL.csv',encoding='utf-8-sig',
          index=False)
