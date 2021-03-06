import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=747269&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.a.get_text())
    print("https://comic.naver.com"+cartoon.a["href"])
