import pandas as pd

review_word = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL.csv')
review_word.info()

Ded = review_word.drop_duplicates(['title'])


Ded.to_csv('./crawling_data/datasets/Game_reviews_ALL_Duplicates.csv',encoding='utf-8-sig',
          index=False)