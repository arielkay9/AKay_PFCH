#Count the number of words in each male speech

import csv
import os

with open('MaleWinners.csv', 'r') as MWinners:
    reader = csv.reader(MWinners)
    header = next(reader)

    header.append('Speech Length')

    updated_rows = []

    for row in reader:
        speech = row[4]
        speech_length = len(speech.split())

        row.append(speech_length)

        updated_rows.append(row)

        with open('MLength.csv', 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(header)
            writer.writerows(updated_rows)