import requests
import pprint

url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'

params = {'q' : 'van gogh',
          'isOnView' : 'true',
          'hasImages' : 'true',
          'ObjectIDs' : '',
          'title' : ''
}

response = requests.get(url, params=params)

if response.status_code == 200:
    object_ids = response.json()['objectIDs']

    for object_id in object_ids:
        object_url = url + '/' + str(object)
        object_response = requests.get(object_url)

        object_data = object_response.json()

    
    pretty = pprint.PrettyPrinter(indent=2)

    pprint(object_data['title'])
