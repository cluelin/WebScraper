from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

browser.find_element_by_id("log.login").click()
