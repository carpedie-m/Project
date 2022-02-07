# from ramen.ramen_code.nongsim import *
# from ramen_code.nongsim import *
# from study.ramen_test.samyang import *
# from study.ramen_test.ottogi import *
# from ramen_test.paldo import *
from stock.stock_code.daily_sise_csvfile import ko_daily_sise


class Main():
    def __init__(self):
        # self.nongsim = nongsim()
        # print("불닭 영양성분-------------------------------")
        # self.samyang = samyang()
        # print("진라면 열량--------------------------------")
        # self.jin = jin()
        # print("팔도비빔면 열량--------------------------------")
        # self.paldo = paldo()
        self.daily_sise_csvfile = ko_daily_sise()
        # print("종목명")



if __name__ == "__main__":
    Main()
