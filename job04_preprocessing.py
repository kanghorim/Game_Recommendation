# 정보처리를 위한 pandas 그리고 한글처리를 위한 konlpy선언
import pandas as pd
from konlpy.tag import Okt
import re

#2. 완성된 csv파일을 불러오고
df = pd.read_csv('./crawling_data/datasets/cleaned_game_Data.csv',index_col= 0)
df.dropna(inplace=True) # 혹시모를 null값이 생기면 안되기때문에 제거
print(df.head()) # 상위 정보 한번 확인
df.info()# 각 컬럼값 개수를 확인하여 null값이 제거 되었는지 확인한다.

#3. 점수 컬럼을 str형식으로 변경하기
df['scores'] = df['scores'].astype(str)
print(df.iloc[-1])
df.info()

#4. crawling_data폴더 안에 stopwords를 불러온다
stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword']) # stopwords파일은 한글의 불용어가 전부 들어가있다.
cleaned_sentences = []
for review in df.reviews: # cleaned_game_Data안에 리뷰를 하나 하나 뜯어서 불용어를 제거한다.
    review = re.sub('[^가-힣 ]', '', review)
    review_word = review.split(' ') # 불용어는 띄어쓰기로 바꾸기

    words = []
    for word in review_word: # 불용어 처리된 review_word를 하나씩 뜯어서
        if len(word) > 1: #길이가 1 이상이면서
            if word not in stopwords_list: # stopwords 파일의 리스트에 없으면
                words.append(word) # words라는 리스트에 추가한다.
    cleaned_sentence = ' '.join(words) # 그리고 join함수를 이용해서 cleaned_sentence라는 새로운 컬럼을 생성
    cleaned_sentences.append(cleaned_sentence) # cleaned_sentence에 cleaned_sentence를 append시켜주고
df['cleaned_sentences'] = cleaned_sentences #df 안에 cleaned_sentence를 추가고
df = df[['title', 'cleaned_sentences','scores','genres']] # 기존의 reviews를 cleaned_sentences로 체인지
df.to_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing.csv', #crawling_data안에 datasets폴더 안에 Game_reviews_ALL_Preprocessing라는
          index=False) # 전처리도 하고 불용어도 제거한 컬럼을 추가함
df.info()