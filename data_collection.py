import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import regex as re

parl1 = ['08-12-1965', '13-12-1965', '16-12-1965', '17-12-1965', '20-12-1965', '21-12-1965', '22-12-1965', '23-12-1965',
         '24-12-1965', '28-12-1965', '29-12-1965', '30-12-1965', '31-12-1965', '23-2-1966', '21-4-1966', '22-6-1966',
         '17-8-1966', '26-8-1966', '26-10-1966', '5-12-1966', '12-12-1966', '14-12-1966', '15-12-1966', '16-12-1966',
         '19-12-1966', '20-12-1966', '21-12-1966', '27-2-1967', '13-3-1967', '14-3-1967', '15-3-1967', '16-3-1967',
         '17-3-1967', '24-5-1967', '29-6-1967', '7-9-1967', '8-9-1967', '31-10-1967', '2-11-1967', '14-11-1967',
         '30-11-1967', '5-12-1967', '11-12-1967', '14-12-1967', '15-12-1967', '18-12-1967', '19-12-1967', '20-12-1967',
         '21-12-1967', '24-1-1968']

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensures the browser window won't be shown
driver = webdriver.Chrome(options=chrome_options)
driver.get(f'https://sprs.parl.gov.sg/search/#/report?sittingdate={parl1[0]}')
webpage = driver.page_source
soup = BeautifulSoup(webpage, 'html.parser')

meta_tags = soup.find_all('meta')
meta_data = {}

for tag in meta_tags:
    if 'name' in tag.attrs:
        if tag.attrs['name'] in ('Sit_Date', 'Title', 'MP_Speak'):
            name = tag.attrs['name']
            content = tag.attrs.get('content', '')
            meta_data[name] = content

print(meta_data)

exit()

table = soup.find('div', class_='reportTable')
print(table.text.strip())
