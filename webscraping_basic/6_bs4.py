import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling.next_sibling.a.get_text())