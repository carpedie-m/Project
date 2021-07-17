from ramen.nongsim import *
from wang.samyang import *
from wang.jin import *
from wang.paldo import *

class Main():
    def __init__(self):
        print("신라면------------------------------------")
        self.nongsim = nongsim()
        print("불닭 영양성분-------------------------------")
        self.samyang = samyang()
        print("진라면 열량--------------------------------")
        self.jin = jin()
        print("팔도비빔면 열량--------------------------------")
        self.paldo = paldo()


if __name__ == "__main__":
    Main()