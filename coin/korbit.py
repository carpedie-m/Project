import time
import csv
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
korbit_all = []
for num in range(1, int(number) + 1):
    names = driver.find_element(By.XPATH, "//*[@id='cryptosM']/div/div[" + str(num) + "]/div[1]/a/div/div/div[1]").text
    # print(names)
    korbit_all.append(names)
# print(korbit_all)

# 코인 개수 (빈 문자열(공백) 제거)
k = list(filter(None, korbit_all))
# print(len(k))

# 최종 코인 리스트
print(k)

driver.close()

# # csv
# korbit = open('/Users/choeseunghee/Documents/Programming/project/stock/stock-csv/coin_name.csv', 'a', newline="")
# wr = csv.writer(korbit)
# wr.writerows([
#     'korbit'
#     ])
#
# for i in range(len(k)):
#     wr.writerow([                             # len() : 문자열의 길이 구하기, 리스트에 들어있는 요소가 몇 개인지 알 수 있음
#         k[i]
#         ])
#
# korbit.close()