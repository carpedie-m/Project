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
korean_name = []
for j in json_obj:
    # print(j)  # dictionary
    korean_name.append(j['korean_name'])
# print(korean_name)

# 새로운 딕셔러니
z = dict(zip(market, korean_name))
# print(z)

# 특정 문자열 포함하는 ticker 리스트
KRW = []
for krw in market:
    if 'KRW-' in krw:
        KRW.append(krw)
        # print(krw)
# print(KRW)
# print(len(KRW)) # KRW 코인 개수

# 특정 문자를 포함하는 key의 value 출력
last = []
for key, value in z.items():
    # print(key, value) # 키-값 확인
    for o in range(len(KRW)):
        if key == KRW[o]:
            # print(value)  # value
            last.append(value)
print(last)
# print(len(last)) # KRW 코인 개수 확인












