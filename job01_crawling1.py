from selenium import webdriver
import pandas as pd
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('lang=ko_KR')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=option)
driver.implicitly_wait(1)

titles = []
reviews = []
scores = []
genres = []
url = 'https://play.google.com/store/apps/collection/cluster?clp=ogouCAESBEdBTUUaHAoWcmVjc190b3BpY19ZYWtDeDlSSTNibxA7GAMqAggCUgIIAg%3D%3D:S:ANO1ljI7UYE&gsr=CjGiCi4IARIER0FNRRocChZyZWNzX3RvcGljX1lha0N4OVJJM2JvEDsYAyoCCAJSAggC:S:ANO1ljLZvWI&hl=ko&gl=US'
driver.get(url)
print(url)

#//*[@id="fcxH9b"]/div[4]/c-wiz[4]/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[61]/div/div/div[1]/div/div/a
#//*[@id="fcxH9b"]/div[4]/c-wiz[4]/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a
game_title = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[{}]/c-wiz/div/div/div[1]/div/div/a'

#poRVub


game_more_view = '//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[6]/div/span/span'
game_title_xpath = '//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1'
score_xpath = '#//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/div/div[1]/c-wiz/div[1]/div[1]'
review_xpath = '//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[{}]/div/div[2]/div[2]/span[1]'

genre_xpath = '//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a'
#hrTbp R8zArc 타이틀클래스
#//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a
#//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a

#//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/span[1]
#//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span[1]
#//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[13]/div/div[2]/div[2]/span[1]

for i in range(0,200):
    try: # 페이지 안에 게임이 200개 안되는게 있음
        driver.get(url)
        SCROLL_PAUSE_SEC = 1

        # 스크롤 높이 가져옴
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            time.sleep(0.3)
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 1초 대기
            time.sleep(SCROLL_PAUSE_SEC)

            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        print('debug01')
        game_title = driver.find_elements_by_css_selector(".poRVub")
        game_title[i].click()
        print('debug02')
        time.sleep(0.3)
        #title = driver.find_element_by_xpath(game_title_xpath).text # 게임 타이틀 가져오고
        title = driver.find_element_by_css_selector('.AHFaub').text
        print('debug03')

        print(title) # 타이틀 프린트로 보여주고
        try: # 스코어 없는게 있음
            score = driver.find_element_by_css_selector('.BHMmbe').text # 스코어 가져오고
            print(score) # 스코어 출력 함 해주고
            genre = driver.find_element_by_xpath(genre_xpath).text # 장르 가져오고
            print(genre)
            driver.find_element_by_xpath(game_more_view).click() # 리뷰 더보기 클릭하고
            while True:
                # 끝까지 스크롤 다운
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # 1초 대기
                time.sleep(SCROLL_PAUSE_SEC)

                # 스크롤 다운 후 스크롤 높이 다시 가져옴
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            game_review = []
            for k in range(1,100):
                print("{}번째 리뷰".format(k))
                try:
                    #UD7Dzf
                    review = driver.find_element_by_xpath(review_xpath.format(k)).text
                    game_review.append(review)
                    print(review)
                except:
                    break
            reviews.append(' '.join(game_review))
            scores.append(score)  # 리스트에 추가하고
            genres.append(genre)
            titles.append(title)
            print('debug10')
            print(len(titles))
            print(len(reviews))
            print(len(scores))
            print(len(genres))
            #각 데이터 프레임을 title, reviews,score, genres로 정해줌
            df = pd.DataFrame({'title': titles, 'reviews': reviews, 'scores': scores, 'genres': genres})
            print(df.tail())
            df.to_csv('./crawling_data/reviews_free_game_card_games.csv', encoding='utf-8-sig', index=False)
            # crawling_data폴더 안에 csv파일 생성후 저장 한글깨짐 방지를 위한 utf-8-sig 추가
            print(df.tail())
        except:
            print('erroe02')
            pass
    except:
        print('error01')
        break


