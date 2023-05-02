import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_female_Academy_Award_winners_and_nominees_for_non-gendered_categories'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table_list = soup.find_all('table', class_='wikitable sortable')
result_list = []

for table in table_list:
    headers = []
    header_row = table.find('tr')
    for header in header_row.find_all('th'):
        if 'Name' in header.get_text():
            headers.append(header.get_text(strip=True))
    rows = []
    for row in table.find_all('tr'):
        name_data = []
        if not row.find('th'):
            for idx, cell in enumerate(row.find_all('td')):
                if idx == 0 or 'Name' in headers[idx]:
                    name_data.append(cell.get_text(strip=True))
            if name_data:
                rows.append(name_data)
    if headers and rows:
        result_list.append({'headers': headers, 'rows': rows})

# Write data to a CSV file
with open('female_oscar_winners.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for result in result_list:
        writer.writerow(result['headers'])
        writer.writerows(result['rows'])

print(data)