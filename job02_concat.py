# Crawling0+Crwaling1+Crawling2 의 CSV 합치기

# 1. 모듈 임포트
import pandas as pd
import glob

# 2. 데이터 ................
data_paths = glob.glob('./crawling_data/*')
print(data_paths)

# 3. 데이터 프레임 생성
df = pd.DataFrame()

# 4. 컬럼명 정의 후 합치기(Concat)
for path in data_paths[1:]:
    df_temp = pd.read_csv(path)
    df_temp.columns = ['title', 'reviews','scores','genres'] #
    df = pd.concat([df, df_temp], ignore_index=True,
              axis='rows')
# 5. 데이터 프레임 정보 확인
df.info()

# 6. CSV 포맷으로 저장하기
df.to_csv('./crawling_data/datasets/Game_reviews_ALL.csv',encoding='utf-8-sig',
          index=False)

