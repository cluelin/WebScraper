import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

imeags = soup.find_all("img", attrs={"class" : "thumb_img"})

for idx, image in enumerate(imeags):
    image_url = image["src"]

    if image_url.startswith("//"):
        image_url = "https:" + image_url

    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)