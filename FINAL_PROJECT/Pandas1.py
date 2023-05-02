import pandas as pd
import matplotlib.pyplot as plt

# read in the data from both CSV files
all_data = pd.read_csv('GodResultsAll.csv')
female_data = pd.read_csv('GodResultsF.csv')

# plot the data
fig, ax = plt.subplots()
ax.plot(all_data['Year'], all_data['Winner'], label='All')
ax.plot(female_data['Year'], female_data['Winner'], label='Female')
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Winner')
plt.show()
