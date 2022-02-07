import csv

path = "/Users/choeseunghui/Documents/"
#
f = open(path + 'sample3.csv', 'w', encoding='utf-8', newline="")
wr = csv.writer(f)
wr.writerow([['이름'], ['브랜드'], ['가격']])
wr.writerow([["고추바사삭"], ['굽네'], ["17,000"]])
wr.writerows([['뿌링클'], ['고추마요'], ['후라이드']])
wr.writerows([['뿌링클'], ['고추마요'], ['후라이드']])
# writerow 는 [[ㅇ],[ㅇ]]-> [ㅇ], [ㅇ]로 출력
# writerows 는 [[[ㅇ]],[ㅇ]]-> [ㅇ],ㅇ 으로 출력
# writerows 세로로 출력
f.close()


# r = open(path + 'sample3.csv', 'r', encoding='utf-8', newline="")
# rd = csv.reader(r)
# for i in rd:
#     print(i)
#
# r.close()
