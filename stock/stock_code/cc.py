#
# num = range(1, 40)
#
# for i in num:
#     a = i*8 +3
#     print(a)

# from bs4 import BeautifulSoup
# import requests
# import csv
#
# codes = [236810]
#
# for code in codes:
#     url = f"https://vip.mk.co.kr/newSt/price/daily.php?p_page=1&y1=2021&m1=01&d1=01&y2=2021&m2=12&d2=30&stCode={str(code)}"
#     reponse = requests.get(url)
#     soup = BeautifulSoup(reponse.content, "html.parser", from_encoding="cp949")
#
#     # 등략률
#     rate = soup.find("table", {"width": "670", "class": "table_3"}).find_all("td")[3].text
#     print(rate)
#
#     # 값
#     num = [11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99,
#            107, 115, 123, 131, 139, 147, 155, 163, 171, 179,
#            187, 195, 203, 211, 219, 227, 235, 243, 251, 259,
#            267, 275, 283, 291, 299, 307, 315, 323]
#     for i in num:
#         rate1 = soup.find("table", {"width": "670", "class": "table_3"}).find_all("td")[i].text
#         print(rate1)
#

num = range(1, 40)

for i in num:
    a = i*8
    print(a)
