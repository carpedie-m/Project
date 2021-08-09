from bs4 import BeautifulSoup
import requests

pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

for page in pages:
    url = f"https://finance.naver.com/sise/dividend_list.nhn?&page={str(page)}"
    reponses = requests.get(url)
    soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding='cp949')

#   종목명
#     name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
#     for n in name:
#         print(n.text)

#   수익률
    num = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
           268, 280, 292, 304, 316, 352, 364, 376, 388, 400, 436, 448, 460, 472, 484,
           520, 532, 544, 556, 568, 604, 616, 628, 640, 652, 688, 700, 712, 724, 736,
           772, 784, 796, 808, 820]  # 수익률 관련 num
    # for r in num:
    #     revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[r]
    #    print(revenue.text)

#   "종목명 : 수익률" - for문 출력값들을 리스트로 변환해 zip함수 이용해 여러 개 리스트 동시 출력

    Nameslist = []
    name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
    for n in name:
        # print(n.text)
        Nameslist.append(n.text)
#   print(Nameslist) - 종목명 리스트로 묶음

    Revenuelist = []
    for r in num:
        revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[r]
        Revenuelist.append(revenue.text)
#   print(Revenuelist) - 수익률 리스트로 묶음

    for N, R in zip(Nameslist, Revenuelist):
        print(N, ":", R)


# 25p 종목명 : 수익률
url = f"https://finance.naver.com/sise/dividend_list.nhn?&page=25"
reponses = requests.get(url)
soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding='cp949')

# 25p 수익률 관련 num
num25 = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
         268, 280, 292, 304, 316, 352, 364]

Nameslist25 = []
name25 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
for n25 in name25:
    # print(n25.text)
    Nameslist25.append(n25.text)
# print(Nameslist25)

Revenuelist25 = []
for i in num25:
    revenue25 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i]
    Revenuelist25.append(revenue25.text)
# print(Revenuelist25)

for N25, R25 in zip(Nameslist25, Revenuelist25):
    print(N25, ":", R25)
