#create .csv of wife results

import csv

with open('Oscars_Speech_Data.csv', 'r') as Data, open('wife_results.csv', 'w', newline='') as output_file:
    search_string = 'my wife'.lower()
    processed_csv = csv.DictReader(Data)
    fieldnames = ['Year', 'Category', 'Winner', 'Speech']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in processed_csv:
        if search_string in row['Speech'].lower():
            writer.writerow({'Year': row['Year'], 'Category': row['Category'], 'Winner': row['Winner'], 'Speech': row['Speech']})