import os
import json

with open ('artworks.json', 'r') as f:
    data = json.load(f)

nationalities = {}
for art_piece in data:
    nationality = art_piece['Nationality']
    if isinstance(nationality, list):
        nationality = ', '.join(nationality)
    if nationality not in nationalities:
        nationalities[nationality] = []
    nationalities[nationality].append(art_piece)

if not os.path.exists('res'):
    os.makedirs('res')

for nationality, art_piece in nationalities.items():
    filename = f'res/{nationality}.json'
    with open(filename, 'w') as f:
        json.dump(art_piece, f, indent=2)
