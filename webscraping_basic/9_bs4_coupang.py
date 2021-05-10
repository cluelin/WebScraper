import requests
import re # <- 정규식 사용
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs = {"class" : re.compile("search-product$")})

for item in items:
    item_name = item.find("div", attrs = {"class":"name"}).get_text()
    rate = item.find("em", attrs = {"class":"rating"})
    rate_cnt = item.find("span", attrs = {"class" : "rating-total-count"})
    if rate:
        rate = rate.get_text()
        rate_cnt = rate_cnt.get_text()
    else:
        continue

    print(item_name, rate, rate_cnt)
