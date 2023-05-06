#Create a .csv file with only the female winners, but keeping all the data in the other columns the same (including speech transcript)


import pandas as pd

AllWinners = pd.read_csv('Oscars_Speech_Data2.csv')
FWinners = pd.read_csv('MaleWinners.csv')

FemWinners = pd.merge(AllWinners, FWinners, on=['Winner'], how='left', indicator=True)

FemWinners = FemWinners[FemWinners['_merge'] == 'left_only']

FemWinners = FemWinners.drop(columns=['_merge'])

FemWinners.to_csv('FemaleWinners.csv', index=False)
