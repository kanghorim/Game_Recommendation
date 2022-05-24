# 본격적으로 Word2Vec모델을 생성할 모듈 생성
from gensim.models import Word2Vec
import pandas as pd

#1.Game_reviews_ALL_Preprocessing_2를 불러와서 null값 제거하고 컬럼개수 확인하기
review_word = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
review_word.info()
review_word.dropna(inplace=True)
print(review_word.head())
review_word.info()

#2.score컬럼이 float형식이라 str형식으로바꿔줘야함
review_word['scores'] = review_word['scores'].astype(str)
print(review_word.iloc[-1])
review_word.info()


# 3. Word2Vec학습을 위한 split 함수를 이용한 토큰 생성
cleaned_token_review = list(review_word['cleaned_sentences'])
print(cleaned_token_review[0])
cleaned_tokens = []
for sentence in cleaned_token_review:
    token = sentence.split()
    cleaned_tokens.append(token)
print(cleaned_tokens[0])

# 4. Word2Vec학습을 위한 모델링 그리고 저장
embedding_model = Word2Vec(cleaned_tokens, vector_size = 100, window = 4, min_count = 20, # 각각 100차원 min_count최소 20번 이상
                           # workers cpu개수 epochs = 학습개수 sg = 1 고정
                           workers = 4, epochs = 100, sg = 1)

embedding_model.save('./models/word2vecModel_Game.model')
#print(embedding_model.wv.vocab.key())
#print(len(embedding_model.wv.vocab.key()))