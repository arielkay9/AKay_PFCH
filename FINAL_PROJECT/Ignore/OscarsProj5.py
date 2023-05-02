import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_female_Academy_Award_winners_and_nominees_for_non-gendered_categories'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable sortable'})

rows = []
for table in tables:
    header_row = [header.get_text(strip=True) for header in table.find_all('th')]

    name_index = header_row.index('Name')

    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells:
            name = cells[name_index].get_text(strip=True)
            rows.append(name)

with open('female_oscar_winners.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name'])
    writer.writerows([[name] for name in rows])

print(rows)