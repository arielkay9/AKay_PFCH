#Use Wikipedia API to download female winner data

import requests
from bs4 import BeautifulSoup
import json

WikipediaAPI = 'https://en.wikipedia.org/w/api.php'

params = {'action': 'query',
    'format': 'json',
    'prop': 'extracts',
    'titles': 'List_of_female_Academy_Award_winners_and_nominees_for_non-gendered_categories'
}

FemaleWinners = requests.get(WikipediaAPI, params=params)

data = FemaleWinners.json()

page_id = next(iter(data['query']['pages']))
page_content = data['query']['pages'][page_id]['extract']

print(page_content)