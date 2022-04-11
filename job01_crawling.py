from selenium import webdriver
import pandas as pd
import time

option = webdriver.ChromeOptions()
#option.add_argument('headless')
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
url = 'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c&hl=ko&gl=US'
driver.get(url)
print(url)
SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

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
game_title = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[{}]/c-wiz/div/div/div[1]/div/div/a'
game_more_view = '//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[6]/div/span/span'
game_title_xpath = '//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1'
score_xpath = '#//*[@id="fcxH9b"]/div[4]/c-wiz[5]/div/div[2]/div/div/main/div/div[1]/c-wiz/div[1]/div[1]'
review_xpath = '//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[{}]/div/div[2]/div[2]/span[1]'
genre_xpath = '//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a'
#hrTbp R8zArc 타이틀클래스
#//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a
#//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a


for i in range(1,201):
    try: # 페이지 안에 게임이 200개 안되는게 있음
        driver.find_element_by_xpath(game_title.format(i)).click() # 게임 클릭하고
        time.sleep(0.3)
        #title = driver.find_element_by_xpath(game_title_xpath).text # 게임 타이틀 가져오고
        title = driver.find_element_by_css_selector('.AHFaub').text
        titles.append(title)
        print(title) # 타이틀 프린트로 보여주고
        try: # 스코어 없는게 있음
            score = driver.find_element_by_css_selector('.BHMmbe').text # 스코어 가져오고
            scores.append(score) # 리스트에 추가하고
            print(score) # 스코어 출력 함 해주고
            genre = driver.find_element_by_xpath(genre_xpath).text
            genres.append(genre)
            print(genre)
        except:
            print('별점이 없음')
        try: # 리뷰 없는게 있네?
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


        except:
            print('리뷰가 없음')
    except:
        pass
