import csv
import os

with open('FemaleWinners.csv', 'r') as FWinners:
    reader = csv.reader(FWinners)
    header = next(reader)

    header.append('Speech Length')

    updated_rows = []

    for row in reader:
        speech = row[4]
        speech_length = len(speech.split())

        row.append(speech_length)

        updated_rows.append(row)

        with open('FLength.csv', 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(header)
            writer.writerows(updated_rows)