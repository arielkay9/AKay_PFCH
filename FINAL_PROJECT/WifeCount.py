#count wife results

import csv

wife_results = 0

with open('MaleWinners.csv', 'r') as Data:
    search_string = 'my wife'.lower()
    processed_csv = csv.DictReader(Data)

    for row in processed_csv:
        if search_string in row['Speech'].lower():
            wife_results += 1

print(f"Wife count: {wife_results}")