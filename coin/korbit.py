import time
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# 창 뜨지 않게
options.add_argument('headless')
# 창 크기 조절
options.add_argument('window-size=1920x1080')
# 빠른 화면 렌더링을 위해 GPU를 통해 그래픽 가속함, 이 부분이 크롬에서 버그를 일으키는 현상
options.add_argument("disable-gpu")


s = Service("/Users/choeseunghee/Downloads/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.korbit.co.kr/market")

# 코인 수 크롤링
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div[1]/div[1]/a[2]").click()
number = str(driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div[1]/div[1]/a[2]").text).replace("전체 ", "")

# 코인명 크롤링 리스트
korbit_names = []
for num in range(1, int(number) + 1):
    names = driver.find_element(By.XPATH, "//*[@id='cryptosM']/div/div[" + str(num) + "]/div[1]/a/div/div/div[1]").text
    # print(names)
    korbit_names.append(names)
    filter(None, korbit_names) # 빈 문자열 제거

# tickers
url = 'https://api.korbit.co.kr/v1/ticker/detailed/all'
responses = urllib.request.urlopen(url)
json_dbj = json.load(responses)
# print(json_dbj)


korbit_tickers = []
for t in json_dbj:
    korbit_tickers.append(t)

# print(tickers)

search = '_krw'
for i, word in enumerate(korbit_tickers):
    if search in word:
        # print(word)
        korbit_tickers[i] = word.strip(search).upper()

print(korbit_names)
print(korbit_tickers)

driver.close()
