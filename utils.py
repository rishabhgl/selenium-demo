from dotenv import load_dotenv
import os

from selenium import webdriver


def load_driver(imp_wait = 0, url = "http://www.python.org"):
    load_dotenv()
    options = webdriver.ChromeOptions()
    options.binary_location = os.getenv('CHROME_PATH')

    driver = webdriver.Chrome(options = options)
    driver.implicitly_wait(imp_wait)

    driver.get(url)
    return driver

