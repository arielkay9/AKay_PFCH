#Plot how winners thank their spouses by year and gender

import pandas as pd
import matplotlib.pyplot as plt


MaleWinners = pd.read_csv('MaleWinners.csv')
FemaleWinners = pd.read_csv('FemaleWinners.csv')

DFWife = MaleWinners[MaleWinners['Speech'].str.contains('my wife', case=False)]
DFHusband = FemaleWinners[FemaleWinners['Speech'].str.contains('my husband', case=False)]

WifeYear = DFWife.groupby('Year').size().reset_index(name='Count')
HusbandYear = DFHusband.groupby('Year').size().reset_index(name='Count')

WifeYear['Year'] = WifeYear['Year'].astype(int)
HusbandYear['Year'] = HusbandYear['Year'].astype(int)

plt.plot(WifeYear['Year'], WifeYear['Count'], label='Phrase "My Wife"')
plt.plot(HusbandYear['Year'], HusbandYear['Count'], label='Phrase "My Husband"')

plt.xticks(range(min(WifeYear['Year']), max(WifeYear['Year'])+1, 5))

plt.xlabel('Year')
plt.ylabel('Spouse Count')
plt.title('Oscar Acceptance Speeches Thanking "My Spouse" by Gender of Winner Over Time')
plt.legend()

plt.show()
