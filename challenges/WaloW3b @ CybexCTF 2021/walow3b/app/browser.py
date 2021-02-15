#!/usr/bin/python3

from selenium import webdriver
from time import sleep
from os import environ, devnull
from sys import argv
from redis import Redis

def visit_url(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=options, service_log_path=devnull)
    
    try:
        driver.get("https://127.0.0.1:4000/noExists")
        driver.add_cookie({"name": "flag", "value": environ.get("FLAG"), "httpOnly": True, "sameSite": "None", "Secure": "True"})

        driver.get(url)

        sleep(int(environ.get("BROWSER_SLEEP")))

    except Exception as e:
        print(e)

    finally:
        driver.quit()

if __name__ == "__main__":
    cli = None
    while not cli:
        cli = Redis(environ.get("DB_HOST"), int(environ.get("DB_PORT")))

    while True:
        sleep(int(environ.get("SLEEP_BETWEEN_QUEUE")))

        for entry in cli.keys():
            visit_url(cli.get(entry).decode())
            cli.delete(entry)




