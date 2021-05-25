import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windwo-size = 1920x10800")


browser = webdriver.Chrome(options = options)
browser.maximize_window

url = "https://play.google.com/store/movies/top"

browser.get(url)

interval = 2

pageHeight = browser.execute_script("return document.body.scrollHeight")
index = 0
while True:

    browser.execute_script(f"window.scrollTo(0, {pageHeight})")

    time.sleep(interval)

    nextHeight = browser.execute_script("return document.body.scrollHeight")
    if (pageHeight == nextHeight):
        break
    else:
        pageHeight = nextHeight
        index += 1

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs = {"class": "Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text() 
    print(title)

print(index)



