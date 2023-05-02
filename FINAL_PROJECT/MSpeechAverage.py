#Group the male winners by year and average the number of words in their speeches, by year

import csv
import os
from collections import defaultdict

with open('MLength.csv', 'r') as MWinners:
    reader = csv.DictReader(MWinners)

    speech_lengths = defaultdict(list)
    for row in reader:
        year = int(row['Year'])
        speech_length = int(row['Speech Length'])
        speech_lengths[year].append(speech_length)

averages = {}
for year, lengths in speech_lengths.items():
    average = sum(lengths) / len(lengths)
    averages[year] = average

with open('MLength.csv') as MWinners:
    reader = csv.reader(MWinners)
    header = next(reader)

    header.append('Average Speech Length')

    Average_Speech_Length = []

    for row in reader:
        year = int(row[0])
        speech_length = int(row[5])

        average = averages[year]

        row.append(average)

        Average_Speech_Length.append(row)

with open('MSpeechAverage.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(header)
    writer.writerows(Average_Speech_Length)