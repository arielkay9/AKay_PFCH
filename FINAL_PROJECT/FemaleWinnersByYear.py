import pandas as pd


FemaleWinners = pd.read_csv('FemaleWinners.csv')

DFHusband = FemaleWinners[FemaleWinners['Speech'].str.contains('my husband', case=False)]

HusbandYear = DFHusband.groupby('Year').size().reset_index(name='Count')

print(HusbandYear)