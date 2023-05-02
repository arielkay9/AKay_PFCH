#Graph Speech-Length Averages by Year

import pandas as pd
import matplotlib.pyplot as plt

dfF = pd.read_csv('FSpeechAverage.csv')
dfM = pd.read_csv('MSpeechAverage.csv')

fig, ax = plt.subplots()

ax.plot(dfF['Year'], dfF['Average Speech Length'], label='Female Average Speech Length')
ax.plot(dfM['Year'], dfM['Average Speech Length'], label='Male Average Speech Length')

ax.set_xlabel('Year')
ax.set_ylabel('Average Speech Length')
ax.set_title('Average Oscar Speech Length by Gender Over Time')
    
ax.set_xticks(range(dfF['Year'].min(), dfF['Year'].max()+1, 5))

ax.legend()

plt.show()