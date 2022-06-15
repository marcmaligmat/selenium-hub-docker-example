from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd


import os
import sys
import time

from loguru import logger

try:
    proxy = "102.165.1.59:5432"
    credentials = "gpfc8:usas32wk"

    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")

    if "local" in sys.argv:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, "chromedriver", "chromedriver_v102.exe")
        driver = webdriver.Chrome(path)

    elif "debug" in sys.argv:
        driver = webdriver.Remote(
            command_executor="http://localhost:4555/wd/hub", options=options
        )
    else:
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub", options=options
        )

    # maximize the window size
    # driver.maximize_window()

    url = "https://www.yellowpages.com/search?search_terms=landscaping&geo_location_terms=Fayetteville%2C+NC"
    # url = "https://adamchoi.co.uk/overs/detailed"
    driver.get(url)
    input("Press enter to contnue: ")

except Exception as e:
    logger.exception("Exception error {}", e)

finally:
    driver.close()
    driver.quit()

    logger.success("Scraper Completed")
