#Only female winners

import pandas as pd

AllWinners = pd.read_csv('Oscars_Speech_Data2.csv')
FWinners = pd.read_csv('MaleWinners.csv')

FemWinners = pd.merge(AllWinners, FWinners, on=['Winner'], how='left', indicator=True)

FemWinners = FemWinners[FemWinners['_merge'] == 'left_only']

FemWinners = FemWinners.drop(columns=['_merge'])

FemWinners.to_csv('FemaleWinners.csv', index=False)