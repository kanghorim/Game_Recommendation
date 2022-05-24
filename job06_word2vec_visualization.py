# 1.Word2Vec을 이용해서 나온 유사도를 matplotlib을 이용한 시각화 모듈
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc
import matplotlib as mpl

# 2.한글 폰트가 깨져서 malgun이라는 폰트를 넣어줌
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(
    fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus']=False
rc('font', family=font_name)

# # !apt -qq -y install fonts-nanum
# import matplotlib as mpl
# import matplotlib.font_manager as fm
# fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
# font = fm.FontProperties(fname=fontpath, size=9)
# plt.rc('font', family='NanumBarunGothic')
# mpl.font_manager._rebuild()

# 3.Word2Vec을 불러오고 키워드를 검색을 위한 코드
embedding_model = Word2Vec.load('./models/word2vecModel_Game.model')
print(list(embedding_model.wv.index_to_key)) # Word2Vec안에 있는 key_word를 보여줌
print(len(list(embedding_model.wv.index_to_key))) # key_word 개수 확인
key_word = input('단어를 입력하면 유사도를 보여드립니다.')
sim_word = embedding_model.wv.most_similar(key_word, topn=10) #입력한 유사한 단어 10개선정
print(sim_word)
print(len(sim_word))

#4. 유사도를 시각화 하기위한 코드
vectors = []
labels = []
for label, _ in sim_word:
    labels.append(label)
    vectors.append(embedding_model.wv[label])
df_vectors = pd.DataFrame(vectors)
print(df_vectors.head())

tsne_model = TSNE(perplexity=40, n_components=2,
                  init='pca', n_iter=2500)
new_value = tsne_model.fit_transform(df_vectors)
df_xy = pd.DataFrame({'word':labels,
                      'x':new_value[:, 0],
                      'y':new_value[:, 1]})
print(df_xy)
print(df_xy.shape)
df_xy.loc[df_xy.shape[0]] = (key_word, 0, 0)

plt.figure(figsize=(8, 8))
plt.scatter(0, 0, s=1500, marker='*')
for i in range(len(df_xy.x) - 1):
    a = df_xy.loc[[i, (len(df_xy.x) - 1)], :]
    plt.plot(a.x, a.y, '-D', linewidth=1)
    plt.annotate(df_xy.word[i], xytext=(1, 1),
                 xy=(df_xy.x[i], df_xy.y[i]),
                 textcoords='offset points',
                 ha='right', va='bottom')
plt.show()