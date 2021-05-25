import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

MAX_WAIT = 10
TARGET_URL  = "https://www.ebay.com/itm/203470115150?epid=21040317811&hash=item2f5fc3914e%3Ag%3AeiEAAOSwVChgSSK3&LH_Auction=1"

TimeToSecDict = {'s': 1, 'm':60, 'h':3600, 'd':86400}

def transformTimeToSec(timeLeft):
    timeList = timeLeft.split()
    
    sec = 0
    
    for timeFactor in timeList:
        timeUnit = timeFactor[-1]
        timeCount = int(timeFactor[:-1])
        
        sec += timeCount * TimeToSecDict[timeUnit]
    print(sec)    


options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")


browser = webdriver.Chrome(options = options)

browser.get(TARGET_URL)

bidButton = browser.find_element_by_id("bidBtn_btn").click()

WebDriverWait(browser, MAX_WAIT).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[1]/div[3]/div/div/div[2]/div[1]/span[1]/span/span/span")))

currentPrice = browser.find_element_by_class_name("ui-text-span__BOLD").text

currentPrice = re.findall(r'\\d+', currentPrice[3:-3])[0]

print(currentPrice)

timeLeft = browser.find_element_by_id("_counter_itemEndDate_timeLeft").text

print(timeLeft)
transformTimeToSec(timeLeft)




