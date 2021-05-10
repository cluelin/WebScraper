import requests
from bs4 import BeautifulSoup

url = "http://www.sellcarauction.co.kr/newfront/successfulbid/sb/front_successfulbid_sb_list.do"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

soup.findAll("td", attrs = {"class": "text_middle"})

