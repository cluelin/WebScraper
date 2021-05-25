import time
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()

url = "https://play.google.com/store/movies/top"

browser.get(url)

interval = 2

pageHeight = browser.execute_script("return document.body.scrollHeight")

while True:

    browser.execute_script(f"window.scrollTo(0, {pageHeight})")

    time.sleep(interval)

    nextHeight = browser.execute_script("return document.body.scrollHeight")
    if (pageHeight == nextHeight):
        break;
    else:
        pageHeight = nextHeight

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs = {"class": "Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text() 
    print(title)





