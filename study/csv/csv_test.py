import csv

# 파일 생성
f = open('sample.csv', 'w', encoding="utf-8", newline='')
wr = csv.writer(f)
# wr.writerow([1,2,3])
wr.writerow([['hello'],[4,5,6],[7,8,9],[10,11,12]])
f.close()

# 파일 읽기
f = open('sample.csv','r', encoding='utf-8', newline='')
rd = csv.reader(f)
# print(rd)         # 의미없음

for i in rd:        # 출력
    print(i)

f.close()


