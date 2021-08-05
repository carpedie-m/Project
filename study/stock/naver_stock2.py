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
# for u in range(16, 821):          # for문 안에 soup이 있으면 안된다!
#     if u % 12 == 4:
#         # print(u)
#         revenue = str(soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[u])
#         print(revenue.replace('<td class="num"> </td>', ""))
#
# revenue = str(soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[16])
# revenue1 = str(soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[28])
# revenue2 = str(soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[40])
# revenue3 = str(soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[52])
# revenue4 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[64])
#
#
#
# print(revenue.replace('<td class="num">', "").replace('</td>', ""))
# print(revenue1.replace('<td class="num">', "").replace('</td>', ""))
# print(revenue2.replace('<td class="num">', "").replace('</td>', ""))
# print(revenue3.replace('<td class="num">', "").replace('</td>', ""))
# print(revenue4.replace('<td class="num">', "").replace('</td>', ""))

for i in [16, 28, 40, 52, 64,
          100, 112, 124, 136, 148,
          184, 196, 208, 220, 232,
          ]:
    revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i].text
    print(revenue)

for i in [100, 112, 124, 136, 148]:
    revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i].text
    print(revenue)



# revenue = soup.find("table", {"class": "type_1 tb_ty"})
# print(revenue)

# revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[16]
# revenue1 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[28]
# print(revenue)
# print(revenue1)
# for r in revenue:
#     print(r)
#
# revenue = str(soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[17])
# print(revenue)

# '종목명 : 수익률'
# name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")
# # print(name)
# p = ""
# for n in name[8:]:
#     p = n.text
#     print(p)
#
# for u in range(16, 824):
#     if u % 12 == 4:
#         # print(u)
#         revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[u].text
#         print(revenue)
#         # .replace("&nbsp;", "")
