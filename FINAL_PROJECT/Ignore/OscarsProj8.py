#count God results

import csv

God_results = 0

with open('Oscar_Speech_Data.csv', 'r') as Data:
    search_string = 'Thank God'.lower()
    processed_csv = csv.DictReader(Data)

    for row in processed_csv:
        if search_string in row['Speech'].lower():
            God_results += 1

print(f"God count: {God_results}")