# 결과물을 보여주기 위한 모듈 생성  = metrics와 pickle파일과 Word2Vec의 모델이 필요함
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread, mmwrite
import pickle
from gensim.models import Word2Vec

df_reviews = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
df_reviews.info()


# 1. getRecommendation라는 함수를 선언하고 유사도와 인덱스값을 한번에 보여주는 코드
def getRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    print(len(simScore))
    print(simScore) # 유사도 출력
    simScore = sorted(simScore, key=lambda x:x[1],
                      reverse=True) # 유사도를 sorted함수로 정리
    simScore = simScore[1:11] # 유사도 높은 순서대로 10개 출력
    movieidx = [i[0] for i in simScore] # 10개 출력에 대한 인덱스값도 붙여줌
    recMovieList = df_reviews.iloc[movieidx] #유사도 높은 게임 + 그 게임의 인덱스값까지 보여줌
    return recMovieList.iloc[:, 0]

#2. Word2Vec을 사용하기 위한코드와 비슷한 단어 유사도 10개 추출
Tfidf_matrix = mmread('./models/Tfidf_Game_review01.mtx').tocsr()
with open('./models/tfidf01.pickle', 'rb') as f:
    Tfidf = pickle.load(f)


embedding_model = Word2Vec.load('./models/word2vecModel_Game.model') #Word2Vec의 모델을 불러옴
key_word = input('게임의 장르나 키워드를 입력해주세요 유사한게임을 추천드립니다.')
sim_word = embedding_model.wv.most_similar(key_word, topn=10)# key_word와 비슷한 게임을 10개 추출
sentence = [key_word] * 11 # key_word의 단어를 11개 이상의 유사도를 확인

words = []

for word, _ in sim_word:
    words.append(word)

for i, word in enumerate(words):
    sentence += [word] * (10 - 1)

sentence = ' '.join(sentence)
sentence_vec = Tfidf.transform([sentence])
cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)

# Word2Vec과 Tfidf_matrix를 이용한 종합 게임 추천
recommendation = getRecommendation(cosine_sim)
print(recommendation)