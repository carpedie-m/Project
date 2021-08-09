import requests
from bs4 import BeautifulSoup

codes = ["005930", "088350", "048260"]

for code in codes:

    url = f"https://finance.naver.com/item/main.nhn?code={str(code)}"

    reponses = requests.get(url)
    soup = BeautifulSoup(reponses.content, "html.parser", from_encoding="cp949")
    # from_encoding="cp949" 한글 안 깨지게 하는 코드

    # '상장주식수' 크롤링
    # 상장주식수
    sang = soup.find("div", {"class": "first"}).find_all("th")[2].text
    # print(sang)

    # 값
    sn = soup.find("div", {"class": "first"}).find_all("em")[2].text
    # print(sn)

    print(sang, ":", sn)

    # '배당수익률' 크롤링

    # 배당수익률
    b = soup.find("div", {"id": "tab_con1", "class": "tab_con1"}).findAll(text="배당수익률")

    v = ""
    for l in b:
        v = l.string
        # print(v)

    # 값
    c = soup.find("div", {"id": "tab_con1", "class": "tab_con1"}).find_all("em")[18].text
    # print(c)

    print(v, ":", c)

    # '배당수익률' <span>태그 제거 안됨
    # f = soup.find("div", {"id": "tab_con1", "class": "tab_con1"}).find_all("th")[12]
    #
    # for i in f:
    #     i.extract()
    #     print(i)

    # <span> 태그 제거됨
    c = str(soup.find("table", {"class": "per_table"}).find_all("th")[3].text.strip())
    re = c.replace("(", "").replace(")", "").replace(" ", "") \
        .replace("배당수익률=배당금/현재가x100", "") \
        .replace("배당금은최근결산연도기준의중간배당을포함한총배당금입니다.", "") \
        .replace("l2020.12", "") \
        .strip()
    print(re)

