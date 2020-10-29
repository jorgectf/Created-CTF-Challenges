#!/usr/bin/python3

from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from sys import argv

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-web-security') # Disabling CORS
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(argv[1])

    sleep(10)

except Exception as e:
    print(e)
finally:
    driver.quit()
