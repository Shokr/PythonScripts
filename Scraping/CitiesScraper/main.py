# Cities Scraper - Muhammed Shokr 5-2019

import re
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

country = input("Enter Country Name (ex: Egypt) : ")


url = 'https://www.citypopulation.de/{}-Cities.html'.format(country)

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

rows = soup.select('tr[itemtype="http://schema.org/City"]')

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '', str_cells))
    list_rows.append(clean2)


df = pd.DataFrame(list_rows)

df1 = df[0].str.split(', ', expand=True)
df1[0] = df1[0].str.strip('[')
xx = df1

print(xx)


export_csv = df1.to_csv('data/cities.csv', mode='w', encoding='utf-8',
                        index=True, index_label='id',
                        header=['city_name_en', 'city_name_ar', 'government', 'population', 'area'],
                        columns=[1, 2, 3, 6, 7])

################################################################################################################
