import json
import urllib.request

url = 'https://api.coinone.co.kr/ticker/?currency=all'
responses = urllib.request.urlopen(url)
json_obj = json.load(responses)
# print(json_obj) # 바로 dict

coinone_tickers = []
for t in json_obj:
    # print(t) # dict for문 --> key, str
    coinone_tickers.append(t.upper())
del coinone_tickers[0:3]

print(coinone_tickers)
