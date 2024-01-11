from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import pandas as pd

# Defining browser and adding "-headless" argument
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
url = 'https://sprs.parl.gov.sg/'
driver.maximize_window()
driver.get(url)

select_element = driver.find_element(By.CSS_SELECTOR, 'select.form-control.ng-untouched.ng-pristine.ng-valid')
select = Select(select_element)
select.select_by_value('1: 1')

# Click the search button
search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
search_button.click()

container = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.container-fluid')))

print(container.text.strip())

search_results = container.find_elements(By.CSS_SELECTOR, "a[class*=_ngcontent]")

for result in search_results:
    print(result.text)
