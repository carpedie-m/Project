import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# 창 뜨지 않게
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
# print(number) # 190 : 페이지에 적힌 개수

bithumb_all = []
for num in range(1, int(number) + 1):
    names = driver.find_element(By.XPATH, '//*[@id="sise_list"]/tbody/tr[' + str(num) + ']/td[1]/div/p/a/strong').text
    # print(names)
    bithumb_all.append(names)
# print(bithumb_all)

# 코인 개수 (빈 문자열(공백) 제거)
b = list(filter(None, bithumb_all))
# print(len(b))

# 최종 코인 리스트
print(b)

driver.close()

# # csv
# bithumb = open('/Users/choeseunghee/Documents/Programming/project/stock/stock-csv/coin_name.csv', 'w', newline="")
# wr = csv.writer(bithumb)
# wr.writerow([
#     'Bithumb'
#     ])
#
# for i in range(len(b)):
#     wr.writerow([                             # len() : 문자열의 길이 구하기, 리스트에 들어있는 요소가 몇 개인지 알 수 있음
#         b[i],
#         ])
#
# bithumb.close()

