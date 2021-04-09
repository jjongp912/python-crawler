import time

from selenium import webdriver
url = "http://www.goobne.co.kr/store/search_store.jsp"
wd = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
wd.get(url)
time.sleep(3)
html = wd.page_source
print(html)

wd.close()
