
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()

# browser.get("http://www.baidu.com")
# print(browser.page_source)
# browser.close()

'''
browser.get("http://ww.taobao.com")
inoput_first = browser.find_element_by_id("q")
intput_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
print(intput_second)
print(input_third)
browser.close()
'''

browser.get("http://www.taobao.com")
input_str = browser.find_element_by_id("q")
input_str.send_keys("watch")
time.sleep(1)
input_str.clear()
input_str.send_keys("MacBook pro")
button = browser.find_element_by_class_name("btn_search")
button.click()
time.sleep(2)
browser.close()
