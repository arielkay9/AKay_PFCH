#Count the number of female winners who use the phrase "Thank God"

import csv

God_results = 0


with open('FemaleWinners.csv', 'r') as Data:
   search_string = 'thank god'.lower()
   processed_csv = csv.DictReader(Data)


   for row in processed_csv:
       if search_string in row['Speech'].lower():
          God_results += 1


print(f"God results: {God_results}")