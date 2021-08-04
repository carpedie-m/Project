from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/sise/dividend_list.nhn?&page=1"
reponses = requests.get(url)
soup = BeautifulSoup(reponses.content, "html.parser")

# 종목명
name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")
# print(name)
p = ""
for n in name[8:]:
    p = n.text
    print(p)

# 수익률

for u in range(16, 821):
    if u % 12 == 4:
        # print(u)
        revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[u].text.strip()
        print(revenue)

# revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[16]
# revenue1 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[28]
# print(revenue)
# print(revenue1)
# for r in revenue:
#     print(r)

# '종목명 : 수익률'
name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")
# print(name)
p = ""
for n in name[8:]:
    p = n.text
    print(p)

for u in range(16, 824):
    if u % 12 == 4:
        # print(u)
        revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[u].text
        print(revenue)
        # .replace("&nbsp;", "")
