from bs4 import BeautifulSoup
import requests

class jin():
    def __init__(self):
        self.extract()

    def extract(self):
        url = "http://ottogi.co.kr/product/product_view.asp?page=1&hcode=&mcode=&stxt=&orderby=BEST&idx=37"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        c = soup.find("table", {"class": "bordered vtbl nutrientTbl"}).text
        # print(c)

        c1 = soup.find("table", {"class": "bordered vtbl nutrientTbl"}).find_all("td")[0].text
        print(c1) #진라면 순한맛 열량
