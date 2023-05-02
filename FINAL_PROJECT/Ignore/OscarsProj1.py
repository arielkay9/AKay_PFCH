#create dictionary with speeches containing the phrase "my wife"

import csv

wife_results = {}

with open('Oscars_Speech_Data.csv', 'r') as Data:
    search_string = 'my wife'.lower()
    processed_csv = csv.DictReader(Data)

    for row in processed_csv:
        if search_string in row['Speech'].lower():
           print(f"Speech: {row['Speech']}\nYear: {row['Year']}\nCategory: {row['Category']}\n")
