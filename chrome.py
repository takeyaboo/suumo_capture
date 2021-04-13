import chromedriver_binary
from selenium import webdriver
import sys

driver = webdriver.Chrome()

# suumoの検索結果を格納する
url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13112&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1'
driver.get(url)

elem_url=[]

elems = driver.find_elements_by_class_name('js-cassette_link_href')

# print(elems)

for elem in elems:
    elem_url.append(elem.get_attribute("href"))

i = 1
for url in elem_url:
    driver.get(url)

    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")

    driver.set_window_size(w,h)

    driver.save_screenshot('./img/img'+ str(i) +'.png')
    i += 1
    driver.back()

driver.quit()
