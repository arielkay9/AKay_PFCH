import pandas as pd

# read the CSV file into a pandas DataFrame
df = pd.read_csv('Oscar_Speech_Data.csv')

# count the number of times "my wife" appears in the "Speech text" column
count = df['Speech'].str.count('my wife', case=False).sum()

# print the result
print(f"The phrase 'my wife' appears {count} times in the Speech text column.")
