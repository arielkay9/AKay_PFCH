import pandas as pd


MaleWinners = pd.read_csv('MaleWinners.csv')


DFWife = MaleWinners[MaleWinners['Speech'].str.contains('my wife', case=False)]


WifeYear = DFWife.groupby('Year').size().reset_index(name='Count')


print(WifeYear)