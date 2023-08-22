from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 인기 급상승 페이지 접속
driver.get("https://www.youtube.com/feed/trending")
time.sleep(2)

def scroll_fun():
    while True:
        # 스크롤 하기 전 높이 
        before_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 현재 높이 만큼 스크롤 내리기 
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        break
#무한 스크롤 함수 호출
scroll_fun()
 

# 제목 요소 가져오기 
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
#제목 저장을 위한 리스트 
title_list = []

#조회수 저장을 위한 리스트
hits_list = []

for title in titles:
    # short 영상, YouTube 영화, 제목데이터 없는 컨텐츠
    if title.get_attribute("aria-label")and title.text and "YouTube 영화" not in title.get_attribute("aria-label"):
        # aria-label 속성값 가져오기
        aria_label =title.get_attribute("aria-label")
        print(aria_label)
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        #조회수 값 범위에 따라 분리
        #조회수 없는 영상은 0으로 조회수 1000미만인 영상은 ,처리 생략
        #조회ㅏ수 1,000이상영상
        if "," in hits:
            hits = int(hits.replace(",",""))
            #조회수 없는 영상
        elif not hits:
            hits=0
        #조회수 1000미만    
        else:
            hits = int(hits)
        
        #동일안 제목영상은 한번만
        if title.text not in title_list:
             title_list.append(title.text)
             hits_list.append(hits)   

#제목, 조회수 리스트가 담긴 딕셔너리
crawling_result = {
    "title":title_list,
    "hits": hits_list
    }
okt = Okt()
word_list = []
for text in title_list:
  
    for word, tag in okt.pos(text):
        if tag in ['Noun', 'Adjective']: # 명사랑 형용사만
        # print(word, tag)
          word_list.append(word)




# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(5):
    words.append(word)

# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(5)]
plt.bar(words, counts)
plt.show()

# 워드클라우드 객체 생성
wc = WordCloud(font_path='malgun',width=400,height=400)

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으므로 생략
# 결과를 이미졸 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()  
wc.to_file('wordcloud_result.png')






result = pd.DataFrame(crawling_result)
result.to_csv("./result123.csv",encoding="utf-8-sig")
result.sort_values(by=["hits"], ascending=False).to_csv("./result123.csv", encoding="utf-8-sig")

     