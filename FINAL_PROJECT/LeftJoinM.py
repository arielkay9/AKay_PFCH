#Create a .csv file with only the male winners, but keeping all the data in the other columns the same (including speech transcript)

import pandas as pd

AllWinners = pd.read_csv('Oscars_Speech_Data2.csv')
FWinners = pd.read_csv('FemaleWinners2.csv')

MWinners = pd.merge(AllWinners, FWinners, on=['Winner'], how='left', indicator=True)

MWinners = MWinners[MWinners['_merge'] == 'left_only']

MWinners = MWinners.drop(columns=['_merge'])

MWinners.to_csv('MaleWinners.csv', index=False)
