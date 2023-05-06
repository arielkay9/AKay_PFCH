import requests
from bs4 import BeautifulSoup

url = 'https://www.moma.org/artists/?exhibition_id=5224&page=1'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

artist_list = soup.find_all('li', class_='grid-item')

for artist in artist_list:
    # Extract artist name
    artist_name = artist.find('h3', class_='typography').text.strip()
    
    # Extract artist bio
    artist_bio = artist.find('p', class_='typography--small').text.strip() if artist.find('p', class_='typography--small') else 'No bio available'
    
    # Extract artist works
    artist_works_list = artist.find_all('p', class_='text--caption')
    if artist_works_list:
        artist_works = [work.text.strip() for work in artist_works_list]
    else:
        artist_works = ['No works available']
    
    # Print artist information
    print('Artist Name:', artist_name)
    print('Artist Bio:', artist_bio)
    print('Artist Works:', artist_works)
