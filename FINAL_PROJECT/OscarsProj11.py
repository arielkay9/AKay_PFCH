#print csv of husband results

import csv

with open('Oscar_Speech_Data.csv', 'r') as Data, open('husband_results.csv', 'w', newline='') as output_file:
    search_string = 'my husband'.lower()
    processed_csv = csv.DictReader(Data)
    fieldnames = ['Year', 'Category', 'Winner', 'Speech']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in processed_csv:
        if search_string in row['Speech'].lower():
            writer.writerow({'Year': row['Year'], 'Category': row['Category'], 'Winner': row['Winner'], 'Speech': row['Speech']})