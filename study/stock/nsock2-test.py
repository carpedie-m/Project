from bs4 import BeautifulSoup
import requests

# headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
#                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

codes = [1]
    # , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    #      21, 22, 23, 24]

for code in codes:

    url = f"https://finance.naver.com/sise/dividend_list.nhn?&page=1"

    reponses = requests.get(url)
    soup = BeautifulSoup(reponses.content, "html.parser", from_encoding="cp949")

    # 종목명
    name = soup.find('table', {"class": "type_1 tb_ty"}).find_all("a")
    # name = soup.find('div', {"class": "bnd_wid"}).find_all("a")
    # print(name)


    for n in name[8:]:
        # p = n.text
        # print(p)

    # 수익률
    for i in [16, 28, 40, 52, 64,
              100, 112, 124, 136, 148,
              184, 196, 208, 220, 232,
              268, 280, 292, 304, 316,
              352, 364, 376, 388, 400,
              436, 448, 460, 472, 484,
              520, 532, 544, 556, 568,
              604, 616, 628, 640, 652,
              688, 700, 712, 724, 736,
              772, 784, 796, 808, 820]:
        revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i].text
        # print(revenue)

    print(n, ":", revenue)

# # 25p
# url = f"https://finance.naver.com/sise/dividend_list.nhn?&page=25"
#
# reponses = requests.get(url)
# soup = BeautifulSoup(reponses.content, "html.parser", from_encoding="cp949")
#
# # 종목명
# name = soup.find('table', {"class": "type_1 tb_ty"}).find_all("a")
# # name = soup.find('div', {"class": "bnd_wid"}).find_all("a")
# # print(name)
# p = ""
# for n in name[8:]:
#     p = n.text
#     print(p)
#
#     # 수익률
# for i in [16, 28, 40, 52, 64,
#           100, 112, 124, 136, 148,
#           184, 196, 208, 220, 232,
#           268, 280, 292, 304, 316,
#           352, 364, 376, 388, 400,
#           436, 448, 460, 472, 484,
#           520, 532, 544, 556, 568,
#           604, 616, 628, 640, 652,
#           688, 700, 712, 724, 736,
#           772, 784
#           ]:
#           revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i].text
#           print(revenue)