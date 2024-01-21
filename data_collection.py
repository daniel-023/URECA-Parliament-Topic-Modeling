import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import regex as re


chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensures the browser window won't be shown

driver = webdriver.Chrome(options = chrome_options)
driver.get('https://sprs.parl.gov.sg/search/#/topic?reportid=022_19680124_S0003_T0008')

webpage = driver.page_source
soup = BeautifulSoup(webpage, 'lxml')
meta_tags = soup.find_all('meta')
meta_data = {}

for tag in meta_tags:
    if 'name' in tag.attrs:
        if tag.attrs['name'] in ('Sit_Date', 'Title', 'MP_Speak'):
            name = tag.attrs['name']
            content = tag.attrs.get('content', '')
            meta_data[name] = content

print(meta_data)

table = soup.find('div', class_='reportTable')
print(table)
exit()


"""
print(soup.find_all('h1')[0].text)  # h[n], n = size of text

print(len(soup.find_all('h1')))  # Number of h1 tags

for i in soup.find_all('h2'):
    print(i.text.strip())

print("P tags:")
for i in soup.find_all('p'):
    print(i.text.strip())
"""

# Analysing each company profile on the webpage
report = soup.findall('div', class_='reportTable')
print(report)  # Visualise the company sections
exit()




print(len(company))  # Prints number of companies on the page
name = []
rating = []
reviews = []
ownership = []
for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('span', class_='companyCardWrapper__companyRatingValue').text.strip())
    reviews.append(i.find('span', class_='companyCardWrapper__ActionCount').text.strip())

    # Extract ownership information
    ownership_text = i.find('span', class_='companyCardWrapper__interLinking').text.strip()
    ownership_match = re.search(r'\b(Public|Private)\b', ownership_text)
    if ownership_match:
        ownership.append(ownership_match.group(0))
    else:
        ownership.append('Private')

data = {'Name': name, 'Rating': rating, 'Reviews': reviews, 'Ownership': ownership}
df = pd.DataFrame(data)
print(df)


