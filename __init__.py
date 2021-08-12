from ramen.nongsim import *
from study.ramen_test.samyang import *
from study.ramen_test.ottogi import *
# from ramen_test.paldo import *
# from study.csv.daily_sise_csvfile import *
from study.stock.allocation_csvfile import kor_allocation

class Main():
    def __init__(self):
        # self.nongsim = nongsim()
        # print("불닭 영양성분-------------------------------")
        # self.samyang = samyang()
        # print("진라면 열량--------------------------------")
        # self.jin = jin()
        # print("팔도비빔면 열량--------------------------------")
        # self.paldo = paldo()
        # self.kor_daily_sise = kor_daily_sise()
        self.kor_allocation = kor_allocation()


if __name__ == "__main__":
    Main()
