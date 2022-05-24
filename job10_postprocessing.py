# 기존의 stopwords에 추가적으로로 넣을 불용어를 추가할 코드
# 이 코드로 단어를 추가하지 않으면 모든 cleaned_sentences안에 많이 포함된 단어가 삭제가 안되서
# 게임 추천이 잘 안됨
import pandas as pd

#1. 전처리가 완료된 csv파일을 불러오기
df = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Preprocessing_2.csv')
df.dropna(inplace=True)
print(df.head())
df.info()

#2.stopwords에 cleaned_sentences안에 있는 너무 큰 비중을 차지한 단어를 불용어에 추가할것
stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_sentences = []
stopwords_movie = ['게임', '좋다','있다','없다','같다','리뷰','해주다','이다','재밌다','되다',
                   '있다','것','정도','오다','이건']
stopwords_list = stopwords_list + stopwords_movie
# 기존에 있던 cleaned_sentences를 추가된 불용어로 다시 한번더 삭제
for review in df.cleaned_sentences:
    review_word = review.split(' ')

    words = []
    for word in review_word:
        if len(word) > 1:
            if word not in stopwords_list:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
df.dropna(inplace=True)
# 추가된 불용어삭제로 인한 더 완벽한 전처리 데이터를 생성 그 후 이 파일을 이용해서 job04번부터 다시 시작하면 더 깔끔한 추천알고리즘이 적용됨
df.to_csv('./crawling_data/datasets/Game_reviews_ALL_Post.csv',encoding='utf-8-sig',
          index=False)
df.info()
print('end')