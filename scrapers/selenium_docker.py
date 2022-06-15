from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd


import os
import sys
import time

from loguru import logger

try:

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
    driver.maximize_window()

    website = "https://adamchoi.co.uk/overs/detailed"

    # driver.get(website)

    # all_matches_button = driver.find_element_by_xpath(
    #     '//label[@analytics-event="All matches"]'
    # )

    # all_matches_button.click()

    # box = driver.find_element_by_class_name("panel-body")

    # dropdown = Select(box.find_element_by_id("country"))
    # dropdown.select_by_visible_text("Spain")
    # time.sleep(5)

    # matches = driver.find_elements_by_css_selector("tr")

    # all_matches = [match.text for match in matches]

    # df = pd.DataFrame({"goals": all_matches})
    # print(df)
    # df.to_csv("test.csv", index=False)


except Exception as e:
    logger.exception("Exception error {}", e)

finally:
    driver.close()
    driver.quit()

    logger.success("Scraper Completed")
