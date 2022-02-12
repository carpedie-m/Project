# 업비트 openAPI - REST API > QUOTATION API : 마켓 코드 조회
import json
import urllib.request

# json 형식 불러오기
json_url = "https://api.upbit.com/v1/market/all?isDetails=false"
json_response = urllib.request.urlopen(json_url)
json_obj = json.load(json_response)
# print(json_obj) # list 속 dictionary

# tickers
market = []
for j in json_obj:
    # j.pop('english_name') # english_name key:value 제거
    # print(j) # dictionary
    # print(j['market']) # dictionary[key1] -> value1 출력
    market.append(j['market'])
# print(market)

# print(json_obj) # korean_name만 남음

# 코인 한글명
k_name = []
for j in json_obj:
    # print(j)  # dictionary
    k_name.append(j['korean_name'])
# print(korean_name)

# 새로운 딕셔러니
z = dict(zip(market, k_name))
# print(z)

# 특정 문자열 포함하는 ticker 리스트
upbit_tickers = []
for krw in market:
    if 'KRW-' in krw:
        upbit_tickers.append(krw)
        # print(krw)
# print(KRW)

# 특정 문자를 포함하는 key의 value 출력
upbit_names = []
for key, value in z.items():
    # print(key, value) # 키-값 확인
    for o in range(len(upbit_tickers)):
        if key == upbit_tickers[o]:
            # print(value)  # value
            upbit_names.append(value)
# print(korean_names)

# 리스트 요소 속 특정 문자부분 제거
search = 'KRW-'
for i, word in enumerate(upbit_tickers): # enumerate 인덱스와 원소 차례 접근하게 해주는 반복자
    # print(i) # 리스트 인덱스-숫자
    # print(word) # 리스트 요소
    if search in word:
        # print(word)
        upbit_tickers[i] = word.strip(search)
# print(tickers)

print(upbit_names)
print(upbit_tickers)
