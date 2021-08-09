import csv

path = '/Users/choeseunghui/Documents/'

# 파일생성
# f = open(path + 'sample2.csv', 'w', encoding="utf-8", newline="")
# wr = csv.writer(f)
# wr.writerow(['이름','나이','성별'])
# wr.writerow(['최승희', '20', '여'])
# wr.writerows([['최영철'],['김떡순'],['왕튀김']])
# wr.writerows([['18'],['16'],['14']])
# f.close()

# 나이 밑으로 writerows 써서 세로로 하는 방법 있나?


# 파일 읽기
r = open(path + 'sample2.csv', 'r', encoding='utf-8', newline="")
rd = csv.reader(r)
# print(rd) 의미없음
for i in rd:
    print(i)       # 출력

r.close()