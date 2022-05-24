
#1. 중복제거를 위한 판다스 모듈 생성
import pandas as pd

#2.job02번에 csv합치기 코드를 실행을 시켰으면 Game_reviews_ALL파일이 생김
review_word = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL.csv')
review_word.info()

Ded = review_word.drop_duplicates(['title'])
# 게임을 장르마다 크롤링했기 때문에 중복됬을경우가 있다. 그래서 중복제거를 drop_duplicates을 이용하여 제거

Ded.to_csv('./crawling_data/datasets/Game_reviews_ALL_Duplicates.csv',encoding='utf-8-sig',
          index=False)