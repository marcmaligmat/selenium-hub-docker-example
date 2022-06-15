from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "chromedriver", "chromedriver_v102.exe")

website = "https://adamchoi.co.uk/overs/detailed"
driver = webdriver.Chrome(path)
driver.get(website)

# locate a button
all_matches_button = driver.find_element_by_xpath(
    '//label[@analytics-event="All matches"]'
)
# click on a button
all_matches_button.click()

# using the "box" section as a reference to help us locate an element inside
box = driver.find_element_by_class_name("panel-body")
# select dropdown and select element inside by visible text
dropdown = Select(box.find_element_by_id("country"))
dropdown.select_by_visible_text("Spain")
time.sleep(5)

matches = driver.find_elements_by_css_selector("tr")

all_matches = [match.text for match in matches]

driver.quit()

df = pd.DataFrame({"goals": all_matches})
print(df)
df.to_csv("test.csv", index=False)
driver.quit()
