import requests
import json
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

POST_URL = 'http://wave.webaim.org/report#/'

URLS = [line.rstrip('\n') for line in open('urls')]

print(URLS)

i = 0
while i < len(URLS):
	
	print(URLS[i])
	
	driver = webdriver.Firefox()
	
	driver.implicitly_wait(30)
	
	driver.get(POST_URL + URLS[i])
	
	nameSplit = URLS[i].replace("/", "_")
	
	nameSplit1 = nameSplit.replace(":", "_")
	
	fileName = ''.join(str(e) for e in nameSplit1) + '.png'
	
	elem = driver.find_element_by_xpath('//*[@id="tab-details"]')
	
	elem.click()
	
	time.sleep(15)
	
	height = driver.execute_script("return document.getElementById('report').contentWindow.document.getElementsByTagName('body')[0].scrollHeight")
	driver.set_window_size(2717, height)
	print(height)
	
	
	try:
	    driver.get_screenshot_as_file(fileName)		
	except:
	    print("screenshot failed 2")
		
	print("file is: " + fileName)
	
	driver.quit()
	
	i += 1
