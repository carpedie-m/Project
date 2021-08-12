from bs4 import BeautifulSoup
import requests
import csv

class kor_allocation():
    def __init__(self):
        self.path = "/Users/choeseunghui/Documents"     # 파일 다운로드 경로

        self.name = ""      # 1p 종목명 이름들
        self.revenue = ""       # 1p 배당수익률

        self.name_List = []     # 1p 종목명 이름 리스트로 묶음
        self.revenue_List = []      # 1p 배당수익률 리스트로 묶음


        self.kor_allocation()


    def kor_allocation(self):
        # print(self.path)
        pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        for page in pages:

            url = f"https://finance.naver.com/sise/dividend_list.nhn?&page={str(page)}"
            reponses = requests.get(url)
            soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding='cp949')

            self.name_List = []
            self.name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
            for n in self.name:
                # print(n.text)
                self.name_List.append(n.text)
            # print(self.name_List)

            self.revenue_List = []

            num = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
                    268, 280, 292, 304, 316, 352, 364, 376, 388, 400, 436, 448, 460, 472, 484,
                    520, 532, 544, 556, 568, 604, 616, 628, 640, 652, 688, 700, 712, 724, 736,
                    772, 784, 796, 808, 820]

            for i in num:
                self.revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i].text
                # print(self.revenue)
                self.revenue_List.append(self.revenue)
            # print(self.revenue_List)

            for name_all, revenue_all in zip(self.name_List, self.revenue_List):
                print(name_all, revenue_all)

            writer_file = open("/Users/choeseunghui/Documents/allocation1.csv", 'w', newline="")
            wr = csv.writer(writer_file)
            wr.writerow([
                '종목명', '배당수익률(%)'
                ])
            for i in range(len(self.name_List)):
                wr.writerow([                 # len() : 문자열의 길이 구하기, 리스트에 들어있는 요소가 몇 개인지 알 수 있음
                    self.name_List[i],
                    self.revenue_List[i]
                    ])

            writer_file.close()
