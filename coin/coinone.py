import json
import urllib.request


url = 'https://api.coinone.co.kr/ticker/?currency=all'
responses = urllib.request.urlopen(url)
json_obj = json.load(responses)
# print(json_obj) # 바로 dict

# tickers_info = json_obj.pop('xec')['currency']
# print(tickers_info)
tickers = []
for t in json_obj:
    # print(t) # dict for문 --> key, str
    tickers.append(t.upper())

del tickers[0:3]
print(tickers)
