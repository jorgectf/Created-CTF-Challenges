#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import os
from redis import Redis


def visit_url(uAgent, url):

    # Avoid DoS
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-gpu')
    options.add_argument("user-agent=%s" % uAgent)

    driver = webdriver.Remote(
        os.environ.get("CHROME_HUB_URL"), options=options, desired_capabilities=caps,
    )

    try:
        driver.get("http://nginx/signin")

        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.ID, "usernameInput")))
        driver.find_element_by_id("usernameInput").send_keys(
            os.environ.get("ADMIN_BOT_USER"))
        driver.find_element_by_id("passwordInput").send_keys(
            os.environ.get("ADMIN_BOT_PASSWORD"))
        driver.find_element_by_id("submitButton").click()
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.ID, "userAgentInput")))

        driver.get(url)

        sleep(int(os.environ.get("BROWSER_SLEEP")))

    except Exception as e:
        print(e)

    finally:
        driver.quit()


if __name__ == "__main__":
    cli = None
    while not cli:
        cli = Redis("redis")

    while True:
        sleep(int(os.environ.get("SLEEP_BETWEEN_QUEUE")))

        for entry in cli.keys():
            visit_url(entry.decode(), cli.get(entry).decode())
            cli.delete(entry)
