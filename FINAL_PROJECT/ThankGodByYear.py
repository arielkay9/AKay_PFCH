#Plot how winners thank God by year and gender

import pandas as pd
import matplotlib.pyplot as plt


MaleWinners = pd.read_csv('MaleWinners.csv')
FemaleWinners = pd.read_csv('FemaleWinners.csv')

DF_FGod = MaleWinners[MaleWinners['Speech'].str.contains('thank god', case=False)]
DF_MGod = FemaleWinners[FemaleWinners['Speech'].str.contains('thank god', case=False)]

FGod_Year = DF_FGod.groupby('Year').size().reset_index(name='Count')
MGod_Year = DF_MGod.groupby('Year').size().reset_index(name='Count')

FGod_Year['Year'] = FGod_Year['Year'].astype(int)
MGod_Year['Year'] = MGod_Year['Year'].astype(int)

plt.plot(FGod_Year['Year'], FGod_Year['Count'], label='Female Winners')
plt.plot(MGod_Year['Year'], MGod_Year['Count'], label='Male Winners')

plt.xticks(range(min(FGod_Year['Year']), max(FGod_Year['Year'])+1, 5))

plt.xlabel('Year')
plt.ylabel('God Count')
plt.title('Oscar Acceptance Speeches Thanking God by Gender of Winner Over Time')
plt.legend()

plt.show()