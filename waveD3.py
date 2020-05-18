import requests
import json
import sys
import time
#import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

POST_URL = 'http://wave.webaim.org/report#/'

URLS = [line.rstrip('\n') for line in open('urls3')]

print(URLS)

i = 0
while i < len(URLS):
	
	print(URLS[i])
	
	options = Options()
	
	options.set_headless(True)
	
	driver = webdriver.Firefox(options=options)
	
	driver.implicitly_wait(30)
	
	driver.get(POST_URL + URLS[i])
	
	nameSplit = URLS[i].replace("/", "_")
	
	nameSplit1 = nameSplit.replace(":", "_")
	
	fileName = ''.join(str(e) for e in nameSplit1) + '.png'
	
	flags = driver.find_element_by_xpath('//*[@id="tab-details"]')
	
	flags.click()
	
	time.sleep(5)
	
	error = driver.find_element_by_xpath('//*[@id="group_list_error"]')
	
	errors = error.find_elements_by_tag_name('li')
	
	with open("data3", "a+") as file:
		file.write('\n' + URLS[i] + '\nErrors: \n')
	
	for item in errors:
		errorText = item.text
		print(errorText)
		with open("data3", "a+") as file:
			file.write(errorText + '\n')
	
	alert = driver.find_element_by_xpath('//*[@id="group_list_alert"]')
	
	alerts = alert.find_elements_by_tag_name('li')
	
	with open("data3", "a+") as file:
		file.write('\nAlerts: \n')	
	
	for item in alerts:
		alertText = item.text
		print(alertText)
		with open("data3", "a+") as file:
			file.write(alertText + '\n')		
		
	#print(error)
	
	driver.quit()
	
	i += 1
