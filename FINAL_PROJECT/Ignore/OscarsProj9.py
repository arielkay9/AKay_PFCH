#compare 2 .csv files

import csv

with open('God_results.csv', 'r') as GodData:
    reader1 = csv.DictReader(GodData)
    data1 = list(reader1)

with open('FemaleWinners2.csv', 'r') as FemaleWinners:
    reader2 =csv.DictReader(FemaleWinners)
    data2 = list(reader2)

col1 = 'Winner'
col2 = 'Winner'

matches = []

for row1 in data1:
    phrase1 = row1[col1]
    for row2 in data2:
        phrase2 = row2[col2]
        if phrase1 == phrase2:
            match = {'God Data': row1, 'Female Winners': row2}
            matches.append(match)

#print(matches)

with open('GodMatches.csv', 'w', newline='') as GodMatchesCSV:
    writer = csv.writer(GodMatchesCSV)
    writer.writerow(['God Data', 'Female Winners'])
    for match in matches:
        writer.writerow([match['God Data'], match['Female Winners']])