# word_cloud를 이용한 각 게임의 단어수 빈도 확인하기
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from matplotlib import font_manager, rc
import matplotlib as mpl
import numpy as np
from PIL import Image

# 1.한글깨짐 방지를 위한 폰트 넣어주기
fontpath = './malgun.ttf'
font_name = font_manager.FontProperties(
    fname=fontpath).get_name()
mpl.rcParams['axes.unicode_minus']=False
rc('font', family=font_name)

#2. 전처리가 완료된 csv불러오기
df = pd.read_csv('./crawling_data/datasets/Game_reviews_ALL_Post.csv')
print(df.head())

#3. 컬럼에 맞는 게임의 iloc숫자를 넣어서 단어 빈도수 확인
words = df.iloc[6, 1]
print(words)

words = words.split()
print(words)

worddict_1 = collections.Counter(words)
worddict_1 = dict(worddict_1)
print(worddict_1)

#4. 3번의 단어 빈도수를 비교하기위한 코드 (3번과 4번의 게임의 빈도수를 확인하고 추가적인 불용어를 알기쉽게 보기위한것)
words = df.iloc[81, 1]
print(words)

words = words.split()
print(words)

worddict_2 = collections.Counter(words)
worddict_2 = dict(worddict_2)

#5. word_cloud 그래프 생성
wordcloud_img_1 = WordCloud(
    background_color='white', max_words=2000,
    font_path=fontpath).generate_from_frequencies(worddict_1)

wordcloud_img_2 = WordCloud(
    background_color='white', max_words=2000,
    font_path=fontpath).generate_from_frequencies(worddict_2)

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img_1, interpolation='bilinear')
plt.axis('off')

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img_2, interpolation='bilinear')
plt.axis('off')
plt.show()