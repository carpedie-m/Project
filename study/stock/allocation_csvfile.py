from bs4 import BeautifulSoup
import requests
import csv

class kor_allocation():
    def __init__(self):
        self.path = "/Users/choeseunghui/Documents/"

        self.name = ""
        self.revenue = ""

        self.namesList = []
        self.revenueList = []

        self.nn = []
        self.rr = []

        self.revenue_code25 = []

        self.name25 = ""
        self.revenue25 = ""

        self.names_List25 = []
        self.revenue_List25 = []

        self.nn25 = []
        self.rr25 = []

        # self.name_data = []
        # self.revenue_data = []
        #
        self.kor_allocation()

    def kor_allocation(self):

        pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        # pages = [1, 2]

        revenue_code = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
                        268, 280, 292, 304, 316, 352, 364, 376, 388, 400, 436, 448, 460, 472, 484,
                        520, 532, 544, 556, 568, 604, 616, 628, 640, 652, 688, 700, 712, 724, 736,
                        772, 784, 796, 808, 820]

        for page in pages:
            url = f"https://finance.naver.com/sise/dividend_list.nhn?&page={str(page)}"
            reponses = requests.get(url)
            soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding="cp949")

            self.namesList = []
            self.name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
            for n in self.name:
                # print(n.text)
                self.namesList.append(n.text)

            self.revenueList = []
            for r in revenue_code:
                self.revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[r].text
                self.revenueList.append(self.revenue)

            for self.nn, self.rr in zip(self.namesList, self.revenueList):
                print(self.nn, ":", self.rr)

        

        # 25p
        # url = "https://finance.naver.com/sise/dividend_list.nhn?&page=25"
        # reponses = requests.get(url)
        # soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding='cp949')
        #
        # self.revenue_code25 = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
        #                        268, 280, 292, 304, 316, 352, 364]
        #
        # self.names_List25 = []
        # self.name25 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
        # for n25 in self.name25:
        #     # print(n25.text)
        #     self.names_List25.append(n25.text)
        #
        # self.revenue_List25 = []
        # for i in self.revenue_code25:
        #     self.revenue25 = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i]
        #     self.revenue_List25.append(self.revenue25.text)
        #
        # for self.nn25, self.rr25 in zip(self.names_List25, self.revenue_List25):
        #     print(self.nn25, self.rr25)
        #
        # # self.revenue_data = self.rr + self.rr25
        # # self.name_data = self.nn + self.nn25
        # # print(self.revenue_data)
        # # print(self.name_data)

        write_file = open("/Users/choeseunghui/Documents/stock_allocation.csv", 'w', newline="")
        writer = csv.writer(write_file)
        writer.writerow([
            "종목명", "배당수익률(%)"
            ])

        for num in range(50):
            writer.writerow([
                self.namesList[num],
                self.revenueList[num]

                # self.revenue_data[num],
                # self.name_data[num]
                ])

        write_file.close()
