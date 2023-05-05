import requests
import pprint

url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'

params = {'q' : 'van gogh',
          'isOnView' : 'true',
          'hasImages' : 'true',
          'ObjectIDs' : ''

}

response = requests.get(url, params=params)

if response.status_code == 200:
    object_ids = response.json()['objectIDs']
    
    pretty = pprint.PrettyPrinter(indent=2)

    pretty.pprint(object_ids)
