from bs4 import BeautifulSoup
import requests

url = 'https://www.moma.org/artists/?exhibition_id=5224&page=1'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

h3_element = soup.find('h3', class_='typography')

if h3_element is not None:
    artist_names = h3_element.get_text(strip=True)
    print(artist_names)
