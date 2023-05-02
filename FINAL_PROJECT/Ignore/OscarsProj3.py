#Use scraping to get the female winners data

import requests
import csv
import json

endpoint = 'https://en.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'format': 'json',
    'prop': 'extracts',
    'titles': 'List_of_female_Academy_Award_winners_and_nominees_for_non-gendered_categories'
}


response = requests.get(endpoint, params=params)

data = response.json()

page_id = next(iter(data['query']['pages']))
page_content = data['query']['pages'][page_id]['extract']

print(page_content)