from bs4 import BeautifulSoup
import requests

class nongsim():
    def __init__(self):
        self.goods()

    def goods(self):
        url = "http://brand.nongshim.com/shinramyun/main/index"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # title = soup.find("h4", {"class": "titTxt02"}).text
        # print(title)
        #
        # n = soup.find("div", {"class": "productTxt"}).text.strip()
        # print(n)

        a1 = soup.find("div", {"class": "productTxt"}).find_all("span")[2].text
        a2 = soup.find("div", {"class": "productTxt"}).find_all("span")[3].text
        # print(a1)
        # print(a2)

        print(a1 + a2)


