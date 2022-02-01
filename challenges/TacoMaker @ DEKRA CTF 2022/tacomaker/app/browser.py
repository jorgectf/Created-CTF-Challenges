#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from os import environ, devnull
from redis import Redis
from concurrent.futures import ThreadPoolExecutor
import signal


def visit_url(url, redis_entry):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--user-agent=TacoMaker/Reviewer')
    # from Makelaris' baby cached view
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-background-networking')
    options.add_argument('--disable-default-apps')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-sync')
    options.add_argument('--disable-translate')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--metrics-recording-only')
    options.add_argument('--no-first-run')
    options.add_argument('--safebrowsing-disable-auto-update')
    options.add_argument('--media-cache-size=1')
    options.add_argument('--disk-cache-size=1')

    driver = webdriver.Remote(
        environ.get("CHROME_HUB_URL"), options=options
    )
    driver.set_page_load_timeout(int(environ.get("BROWSER_SLEEP")))

    try:
        print("Visiting {}".format(url))
        driver.get(url)
        sleep(int(environ.get("BROWSER_SLEEP")))

    except Exception as e:
        print(e)

    finally:
        driver.quit()
        global entries
        entries.remove(redis_entry)
        cli.delete(redis_entry)


if __name__ == "__main__":
    cli = None
    while not cli:
        cli = Redis(environ.get("REDIS_HOST"))

    print("Waiting for selenium...")
    sleep(20)
    print("Starting browser.py")

    pool = ThreadPoolExecutor(max_workers=int(environ.get("BROWSER_THREADS")))
    entries = []

    while True:
        sleep(int(environ.get("SLEEP_BETWEEN_QUEUE")))
        for entry in cli.keys():
            if not entry in entries:
                entries.append(entry)
                url = cli.get(entry).decode()
                pool.submit(visit_url, url, entry)
