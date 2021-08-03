import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"

reponses = requests.get(url)  # reponses.content
soup = BeautifulSoup(reponses.content, "html.parser")

# '상장주식수' 크롤링

# 상장주식수
sang = soup.find("div", {"class": "first"}).find_all("th")[2].text
# print(sang)

# 값
sn = soup.find("div", {"class": "first"}).find_all("em")[2].text  # 값
# print(sn)

print(sang, ":", sn)

# '배당수익률' 크롤링

# 배당수익률
b = soup.find("div", {"id": "tab_con1", "class": "tab_con1"}).findAll(text="배당수익률")

for l in b:
    v = l.string
    # print(v)

# 값
c = soup.find("div", {"id": "tab_con1", "class": "tab_con1"}).find_all("em")[18].text
# print(c)

print(v, ":", c)

# ## '배당수익률' <span>태그 제거 안됨
# f = soup.find("div", {"id": "tab_con1", "class": "tab_con1"}).find_all("th")[12]
#
# for i in f:
#     i.extract()
#     print(i)
