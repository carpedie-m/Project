from bs4 import BeautifulSoup
import requests

class samyang():
    def __init__(self):
        self.extraction()

    def extraction(self):
        url = "https://www.samyangfoods.com/kor/brand/view.do?seq=53"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.content, "html.parser")
        # print(soup)

        # c = soup.find("div", {"class": "product-view-text area01"}).text.strip()
        # print(c)
        # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        #
        #
        # con = soup.find("div", {"class": "product-view-text area01"}).find_all("p")[0].text.strip()
        # print(con)
        # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")


        con1 = soup.find("div", {"class": "view-table"}).find_all("table")
        for i in con1:
            print(i.text.strip())  # 하나하나 있는 것들 묶으려면 ends()로 #표도 가능하다

        print("ㅡㅡㅡㅡ나트륨 함량ㅡㅡㅡㅡㅡㅡㅡ")
        con2 = soup.find("div", {"class": "view-table"}).find_all("td")[0].text
        print(con2) # 나트륨 함량만









