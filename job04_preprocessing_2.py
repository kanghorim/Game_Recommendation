#1. job04_preprocessing이랑 똑같이 모듈 생성
import pandas as pd
from konlpy.tag import Okt
import re

#2. job04_preprocessing를 통해서 나온 Game_reviews_ALL_Preprocessing csv파일을 불러오고
df = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing.csv')
df.dropna(inplace=True) # 혹시모를 null값이 있다면 제거해준다.
print(df.head())# 상위 데이터 확인후
df.info()# 각 컬럼의 개수를 확인하고

#3.형태소 분류기 사용하기
okt = Okt() # okt라는 형태소 분석기 라이브러리 호출
count = 0
cleaned_sentences = []
for sentence in df.cleaned_sentences: #DataFrame안에 cleaned_sentences를 가져오고
    # 시간이 오래걸리는 작업이라 콘솔창에 진행되고있다는걸 보여주는 코드
    count += 1
    if count % 10 ==0: # 10개 마다 . 하나 찍고
        print('.', end='')
    if count % 100 == 0:# 100개마다 줄바꿈
        print()
    token = okt.pos(sentence, stem=True)# 토큰하나 만들어준 다음
    # print(token)
    df_token = pd.DataFrame(token,  columns=['word', 'class'])
    df_token = df_token[(df_token['class']=='Noun') | # 명사
                                (df_token['class']=='Verb') | # 동사
                                (df_token['class']=='Adjective')] # 형용사로 형태소 분류를 나눠줌
    cleaned_sentence = ' '.join(df_token.word) # 형태소분류 했으니 다시 원래 자리로 넣어주기 위해서 join으로 합쳐줌
    # print(cleaned_sentence)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences  # 형태소 분류가된 cleaned_sentences를 다시 DataFrame에 넣어주고
print(df.head()) # 머리부분 확인하고
df.info() # 혹시 컬럼개수가 바뀌었는지 확인 -> 바뀌진 않았음
df.to_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv',#Game_reviews_ALL_Preprocessing_2라는 csv파일을 하나 생성
          index=False)