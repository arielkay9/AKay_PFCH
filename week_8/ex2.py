import requests
from bs4 import BeautifulSoup

url = 'https://www.moma.org/artists/?exhibition_id=5224&page=1'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

artist_list = soup.find_all('h3', class_='typography')

artists_dict = {}

for artist in artist_list:
    artist_name = artist.text.strip()
    bio = ""
    works = "No works available"
    bio_elem = artist.find_next_sibling('p', class_='typography')
    if bio_elem:
        bio = bio_elem.text.strip()
    works_elem = bio_elem.find_next_sibling('p', class_='typography')
    if works_elem and 'works online' in works_elem.text:
        works = works_elem.text.strip()
    artists_dict[artist_name] = {"bio": bio, "works": works}

print(artists_dict)
