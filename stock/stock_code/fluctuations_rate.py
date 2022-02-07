from bs4 import BeautifulSoup
import requests
import csv


class date_FluctuationsRate():
    def __init__(self):


        # codes = [236810]
        pages = [1]
        # pages = [1, 2, 3, 4, 5]

        for page in pages:
            url = f"https://vip.mk.co.kr/newSt/price/daily.php?p_page={page}&y1=2021&m1=01&d1=01&y2=2021&m2=12&d2=30&stCode=236810"
            reponse = requests.get(url)
            soup = BeautifulSoup(reponse.content, "html.parser", from_encoding="cp949")

            # 등략률
            name = soup.find("table", {"width": "670", "class": "table_3"}).find_all("td")[3].text
            print(name)

            # 날짜
            num_date = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80,
                        88, 96, 104, 112, 120, 128, 136, 144, 152, 160,
                        168, 176, 184, 192, 200, 208, 216, 224, 232, 240,
                        248, 256, 264, 272, 280, 288, 296, 304, 312, 320]

            for j in num_date:
                date = soup.find("table", {"width": "670", "class": "table_3"}).find_all("td")[j].text
                print(date)


            # 값
            num = [11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99,
                    107, 115, 123, 131, 139, 147, 155, 163, 171, 179,
                    187, 195, 203, 211, 219, 227, 235, 243, 251, 259,
                    267, 275, 283, 291, 299, 307, 315, 323]

            for i in num:
                rate = soup.find("table", {"width": "670", "class": "table_3"}).find_all("td")[i].text
                print(rate)


            # 6페이지
            url = f"https://vip.mk.co.kr/newSt/price/daily.php?p_page=6&y1=2021&m1=01&d1=01&y2=2021&m2=12&d2=30&stCode=236810"
            reponse6 = requests.get(url)
            soup6 = BeautifulSoup(reponse6.content, "html.parser", from_encoding="cp949")

            num = [11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99,
                   107, 115, 123, 131, 139, 147, 155, 163, 171, 179,
                   187, 195, 203, 211, 219, 227, 235, 243, 251, 259,
                   267, 275, 283]

            for i in num:
                rate6 = soup6.find("table", {"width": "670", "class": "table_3"}).find_all("td")[i].text
                print(rate6)




