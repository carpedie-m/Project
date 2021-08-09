from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/sise/dividend_list.nhn?&page=1"
reponses = requests.get(url)
soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding='cp949')

# 종목명
# name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
# for n in name:
#     print(n.text)

# 수익률
num = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
       268, 280, 292, 304, 316, 352, 364, 376, 388, 400, 436, 448, 460, 472, 484,
       520, 532, 544, 556, 568, 604, 616, 628, 640, 652, 688, 700, 712, 724, 736,
       772, 784, 796, 808, 820]
# for r in num:
#     revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[r]
#     print(revenue.text)

# 종목명 : 수익률 - for문 출력값들을 리스트로 변환해 zip함수 이용해 여러 개 리스트 동시 출력

Nameslist = []
name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
for n in name:
    # print(n.text)
    Nameslist.append(n.text)
# print(Nameslist) - 종목명 리스트로 묶음


Revenuelist = []
for r in num:
    revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[r]
    Revenuelist.append(revenue.text)
# print(Revenuelist) - 수익률 리스트로 묶음

for N, R in zip(Nameslist, Revenuelist):
    print(N, ":", R)
