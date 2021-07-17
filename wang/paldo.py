from bs4 import BeautifulSoup
import requests

class paldo():
    def __init__(self):
        self.contents()

    def contents(self):
        url = "https://www.paldofood.co.kr/User/Brand/Brand01.asp"
        reponses = requests.get(url)
        soup = BeautifulSoup(reponses.content, "html.parser")

        con1 = soup.find("ul", {"class": "con01_01"})
        print(con1)
