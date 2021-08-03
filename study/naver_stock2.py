from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/sise/dividend_list.nhn"
reponses = requests.get(url)
soup = BeautifulSoup(reponses.content, "html.parser")


