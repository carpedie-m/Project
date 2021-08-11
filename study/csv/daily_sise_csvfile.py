from bs4 import BeautifulSoup
import requests
import csv

class kor_daily_sise():
    def __init__(self):
        self.path = "/Users/choeseunghui/Documents/"

        self.name = ""
        self.rate = ""

        self.name_data = []
        self.rate_data = []

        self.kor_daily_sise()

    def kor_daily_sise(self):

        url = "https://finance.naver.com/sise/sise_group.nhn?type=upjong"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser", from_encoding="cp949")

        name_code = [1, 8, 15, 22, 29,
                39, 46, 53, 60, 67,
                77, 84, 91, 98, 105,
                115, 122, 129, 136, 143,
                153, 160, 167, 174, 181,
                191, 198, 205, 212, 219,
                229, 236, 243, 250, 257,
                267, 274, 281, 288, 295,
                305, 312, 319, 326, 333,
                343, 350, 357, 364, 371,
                381, 388, 395, 402, 409,
                419, 426, 433, 440, 447,
                457, 464, 471, 478, 485,
                495, 502, 509, 516, 523,
                533, 540, 547, 554, 561,
                571, 578, 585, 592]

        self.name_data = []
        for names in name_code:
            self.name = soup.find_all("td")[names].text
            self.name_data.append(self.name)

        rate_code = [2, 9, 16, 23, 30,
                40, 47, 54, 61, 68,
                78, 85, 92, 99, 106,
                116, 123, 130, 137, 144,
                154, 161, 168, 175, 182,
                192, 199, 206, 213, 220,
                230, 237, 244, 251, 258,
                268, 275, 282, 289, 296,
                306, 313, 320, 327, 334,
                344, 351, 358, 365, 372,
                382, 389, 396, 403, 410,
                420, 427, 434, 441, 448,
                458, 465, 472, 479, 486,
                496, 503, 510, 517, 524,
                534, 541, 548, 555, 562,
                572, 579, 586, 593]

        self.rate_data = []
        for rates in rate_code:
            self.rate = soup.find_all("td")[rates].text.strip().replace("%", "")
            self.rate_data.append(self.rate)

        write_file = open("/Users/choeseunghui/Documents/DAILY_SISE22.csv", "w", newline="")
        writer = csv.writer(write_file)
        writer.writerow([
            "업종명", "전일대비(%)"
        ])

        for num in range(79):
            writer.writerow({
                self.name_data[num],
                self.rate_data[num]
            })


        write_file.close()