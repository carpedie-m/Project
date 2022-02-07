from bs4 import BeautifulSoup
import requests
import csv

class kor_allocations():

    def __init__(self):
        self.path = "/Users/choeseunghui/Documents"     # 파일 다운로드 경로

        self.name = ""      # 1p 종목명 이름들
        self.revenue = ""       # 1p 배당수익률

        self.name_list = []     # 1p 종목명 이름 리스트로 묶음
        self.revenue_list  = []      # 1p 배당수익률 리스트로 묶음

        self.kor_allocation()

    def kor_allocation(self):
        # print(self.path)
        pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        # pages = [1]

        for page in pages:

            url = f"https://finance.naver.com/sise/dividend_list.nhn?&page={str(page)}"
            reponses = requests.get(url)
            soup = BeautifulSoup(reponses.content, 'html.parser', from_encoding='cp949')

            self.name_list = []

            self.name = soup.find("table", {"class": "type_1 tb_ty"}).find_all("a")[8:]
            # print(self.name)                          # 페이지 당 50개 요소 있는 한 리스트 - 태그 제거 x
            for n in self.name:                         # 태그 제거 위해 리스트 속 요소들 하나씩 빼기
                # print(n.text)                         # 태그 제거
                self.name_list.append(n.text)           # 태그 제거한 것들 새로운 리스트(self.name_all)에 추가
            # print(self.name_list)

            self.revenue_list = []

            num = [16, 28, 40, 52, 64, 100, 112, 124, 136, 148, 184, 196, 208, 220, 232,
                   268, 280, 292, 304, 316, 352, 364, 376, 388, 400, 436, 448, 460, 472, 484,
                   520, 532, 544, 556, 568, 604, 616, 628, 640, 652, 688, 700, 712, 724, 736,
                   772, 784, 796, 808, 820]         # 'num' - html에서 배당수익률 값에 해당하는 태그 순서

            for i in num:
                self.revenue = soup.find("table", {"class": "type_1 tb_ty"}).find_all("td")[i].text
                # print(self.revenue)
                self.revenue_list.append(self.revenue)
            print(self.revenue_list)                       # 태그 제거하고 새로운 리스트(self.revenue_list)에 추가

            # for name_all, revenue_all in zip(self.name_list, self.revenue_list):
                # print(name_all, ":", revenue_all)

            writer_file = open("allocation1.csv", 'w', newline="")
            wr = csv.writer(writer_file)
            wr.writerow([
                '종목명', '배당수익률(%)'
                ])

            for i in range(len(self.name_list)):
                wr.writerow([                             # len() : 문자열의 길이 구하기, 리스트에 들어있는 요소가 몇 개인지 알 수 있음
                    self.name_list[i],
                    self.revenue_list[i]
                    ])

            writer_file.close()

            # print(종목명 : 배당수익률)는 24페이지 모두 성공, 파일화는 실패
            # 실패 원인 - 열에 넣는 변수('self.name_list', 'self.revenue_list')가 잘못된 듯

            # 'self.name_list'가 한 리스트묶음(50개)밖에 파일에 안 들어감
            # 리스트 24개를 한 리스트로 묶는 방법은 없을까?

