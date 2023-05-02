#count husband results

import csv

husband_results = 0

with open('FemaleWinners.csv', 'r') as Data:
    search_string = 'my husband'.lower()
    processed_csv = csv.DictReader(Data)

    for row in processed_csv:
        if search_string in row['Speech'].lower():
            husband_results += 1

print(f"Husband count: {husband_results}")