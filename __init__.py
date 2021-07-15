from ramen.nongsim import *
from wang.samyang import *
from wang.jin import *

class Main():
    def __init__(self):
        print("신라면--------------------------------")
        self.nongsim = nongsim()
        print("불닭 영양성분--------------------------------")
        self.samyang = samyang()
        print("진라면 열량--------------------------------")

        self.jin = jin()

if __name__ == "__main__":
    Main()