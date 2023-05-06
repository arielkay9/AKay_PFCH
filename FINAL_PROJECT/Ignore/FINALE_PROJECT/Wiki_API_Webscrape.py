#Use wikipedia's API to get all the data from each table into .json and .html files.
#Use BeautifulSoup to scrape that .html file into a .csv.
#Note: I used this same code on each table, adjusting the resulting .csv file name, the "section" param, and the "cell" number where necessary. All the resulting individual .csv files are in the folder CSVs.

from urllib import response
import pandas as pd
import requests
import csv
import json
from bs4 import BeautifulSoup



url = "https://en.wikipedia.org/w/api.php"
subject = "List_of_female_Academy_Award_winners_and_nominees_for_non-gendered_categories"
params = {
    "action" : "parse",
    "page" : subject,
    "section" :21,
    "format" : "json",
    "prop" : "text",
    "redirects" : ""
}

response = requests.get(url, params=params)
data = response.json()

# print(json.dumps(data, indent=2))
with open("res.json", 'w') as f:
    json.dump(data,f,indent=2)

with open("res.html", 'w') as f:
    f.write(data['parse']['text']['*'])

soup = BeautifulSoup(data['parse']['text']['*'])
table = soup.find('table')


rows = table.find_all('tr', attrs={'bgcolor': None})

with open('HumanitarianAward.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Year', 'Name'])
    for person in rows:
        cells = person.find_all('td')
        year = cells[0].text.strip()
        name = cells[1].text.strip()
        #status = cells[3].text.strip()
        #if status.lower() == 'won':
        writer.writerow([year, name])

# for person in rows:
#     cells = person.find_all('td')
#     year = cells[0].text.strip()
#     name = cells[1].text.strip()
#     #film = cells[2].text.strip()
#     status = cells[3].text.strip()
#     #notes = cells[4].text.strip()
#     if status.lower() == "won":
#         writer.writerow({'year: {year},'name: {name}'})
#         print(f'name: {name}, status: {status}')


# print(data)

# raw_html = data["parse"]["text"]["*"]
# soup = BeautifulSoup(raw_html, "html.parser")
# soup.find_all('p')
# text = ""

# for p in soup.find_all("p"):
#     text += p.text

# print(text)
