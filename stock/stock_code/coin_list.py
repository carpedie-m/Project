from bs4 import BeautifulSoup
import requests
import csv

class coin_lists():
    def __init__(self):

        self.path = "/Users/choeseunghee/Documents"
        self.name = ""

    def coin_list(self):

        url = "https://www.korbit.co.kr/market"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser", from_encoding="cp949")

        self.name = soup.find("div", {"id": "cryptosM"})
        print(self.name)





