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
     "format" : "json",
     "prop" : "sections",   
     "redirects" : ""
}

response = requests.get(url, params=params)
data = response.json()

print(json.dumps(data, indent=2))
