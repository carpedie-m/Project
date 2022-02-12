import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# # 창 뜨지 않게
# options.add_argument('headless')
# # 창 크기 조절
# options.add_argument('window-size=1920x1080')
# # 빠른 화면 렌더링을 위해 GPU를 통해 그래픽 가속함, 이 부분이 크롬에서 버그를 일으키는 현상
# options.add_argument("disable-gpu")

s = Service("/Users/choeseunghee/Downloads/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.bithumb.com")

# 코인 수 크롤링
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="realPriceContainer"]/div[1]/dl/dt/a[1]').click() # 원화마켓 클릭
driver.find_element(By.XPATH, '//*[@id="realPriceContainer"]/div[1]/div[2]/dl/dt/a[1]/span')
number = str(driver.find_element(By.XPATH, '//*[@id="realPriceContainer"]/div[1]/div[2]/dl/dt/a[1]/span').text)
# print(number) # 190 : 홈페이지 코인 개수

bithumb_all = []
# tickers_all = []
for num in range(1, int(number) + 1):
    names = driver.find_element(By.XPATH, '//*[@id="sise_list"]/tbody/tr[' + str(num) + ']/td[1]/div/p/a/strong').text
    # print(names)

    # print(ticker)
    bithumb_all.append(names)
    # tickers_all.append(ticker)
# print(bithumb_all)
# print(tickers_all)

# b = list(filter(None, bithumb_all)) # 빈 문자열 제거
# print(b) # 최종 코인 리스트
ticker = driver.find_element(By.XPATH, '//*[@id="coinListTab"]/div/div/div[1]/ol/li[1]/a/div[1]/span[1]')
# two = driver.find_element(By.XPATH, '//*[@id="coinListTab"]/div/div/div[1]/ol/li[3]/a/div[1]/span[1]').text
print(ticker)

driver.close()

