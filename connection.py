import os
from selenium import webdriver
import time
import requests

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

def getstatus():
	response = requests.get("http://www.google.com.sg")
	#print(int(response.status_code))
	return response 



while True:
	response = getstatus()
	disconnected = 'http://sb.login.org/login?dst=http%3A%2F%2Fwww.google.com.sg%2F'
	if response.url == disconnected:
		connected = 0
		driver = webdriver.Chrome(chromedriver)
		driver.get("http://login5.d-synergy.com/starbucks/v3/lpass.php")

		while connected == 0:
			response = getstatus()
			if response.url != disconnected:
				connected =1
				driver.quit()
