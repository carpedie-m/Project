import csv

# path = "/Users/choeseunghui/Documents/Programming/project/stock/stock-csv/"

# csv 생성(쓰기)
f = open('../stock-csv/csv_test.csv', 'w', encoding='utf-8', newline="")
wr = csv.writer(f)

wr.writerow(['이름', '브랜드', '가격']) # 행(가로)
wr.writerows([['뿌링클'], ['고추마요'], ['후라이드']]) # 열(세로)

f.close()

# csv 불러오기(읽기)
r = open('../stock-csv/csv_test.csv', 'r', encoding='utf-8', newline="")
rd = csv.reader(r)
for i in rd:
    print(i)

r.close()

