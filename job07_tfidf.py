# 1.tfidf를 위한 모듈 생성
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

# 2.전처리가 완료된 Game_reviews_ALL_Preprocessing_2를 불러오기
df_reviews = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True) # sublinear_tf이용한 단어빈도의 대한 스무딩 처리 (스무딩 = 블러링과 노이즈 제거)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['cleaned_sentences']) # cleaned_sentences은 train dataset이기 때문에 fit_transform를 사용해서 Tfidf_matrix를 생성

with open('./models/tfidf01.pickle', 'wb') as f: #자연어 처리를 위한 pickle생성
    pickle.dump(Tfidf, f)
mmwrite('./models/Tfidf_Game_review01.mtx', Tfidf_matrix) # 메트릭스 저장을 위해 mmwritegk함수 사용
print('end')