import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Duplicates.csv')
df.dropna(inplace=True)
print(df.head())
df.info()

df['scores'] = df['scores'].astype(str)
print(df.iloc[-1])
df.info()


stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_sentences = []
for review in df.reviews:
    review = re.sub('[^가-힣 ]', '', review)
    review_word = review.split(' ')

    words = []
    for word in review_word:
        if len(word) > 1:
            if word not in stopwords_list:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
df = df[['title', 'cleaned_sentences','scores','genres']]
df.to_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing.csv',
          index=False)
df.info()