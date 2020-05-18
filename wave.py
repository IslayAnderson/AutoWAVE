import requests
import json
import sys



IP_API = 'https://api.ipify.org'

API_KEY = 'AIzaSyC0ouhAV792q6EkG5hOLDG81Z790uTD3Ww'

POST_URL = 'http://wave.webaim.org/report#/'

URLS = [line.rstrip('\n') for line in open('urls')]

ip_address = requests.get(IP_API).text

print(URLS)

i = 0
while i < len(URLS):
  print(URLS[i])
  resp = requests.get(
        POST_URL + URLS[i]
    )
  
  data = resp.content.decode('utf-8')
  
  print(data)
  
  name = URLS[i].split('/')
  
  try:
	  fileName = name[3]
  except:
	  fileName = name[2]
  
  with open(fileName + '.html', "w+") as file:
    file.write(data)
  
  i += 1