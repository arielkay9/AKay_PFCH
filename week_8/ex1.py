import requests
from bs4 import BeautifulSoup

url = 'https://www.moma.org/artists/?exhibition_id=5224&page=1'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

artist_list = soup.find_all('h3', class_='typography')

artist_names = []
for artist in artist_list:
    artist_names.append(artist.text.strip())

print(artist_names)
