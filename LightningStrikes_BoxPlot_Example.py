# TASK: 1. Create a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Make the df have columns for the week number in the year and the day of the week
# 3. Filter the df to only have year 2020 data in it 
# 4. Create and plot a box plot (use sns) of: strike totals per day of the week for the year 2020

#pip install matplotlib
#pip install pandas
#pip install seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D') # create a range of dates from 2020-01-01 to 2024-12-31 ; generated on a daily frequency (each date in the range will be included)

sample_dates = np.random.choice(dates, size=100, replace=False) # randomly sample 100 unique dates from the 'dates' range
lightning_values = np.random.randint(100, 1000, size=len(sample_dates))# randomly generate 100 integers between 100 and 999

df = pd.DataFrame({'date': sample_dates, 'lightning_strikes': lightning_values}) # create a DataFrame with 'sample_dates' as the values for a column 'date' and another column 'lightning_strikes' filled with values from 'lightning_values'
df
         date  lightning_strikes # output ; current date format: yyyy-mm-dd
0  2024-07-04                773
1  2020-07-19                416
2  2020-05-11                462
3  2022-03-20                278
4  2024-10-28                832
..        ...                ...
95 2021-06-08                212
96 2023-09-04                336
97 2020-10-11                541
98 2024-09-25                178
99 2021-05-09                938

[100 rows x 2 columns]

  
df['date'] = pd.to_datetime(df['date']) # converts 'date' column to datetime format (so df['date'] will be dtype: datetime64[ns])

# Create two new columns
df['week'] = df.date.dt.isocalendar().week # week will be between 1-52
df['day_of_the_week'] = df.date.dt.day_name() # day_of_the_week will be Sunday-Saturday

df_2020 = df[df['date'].dt.year == 2020] # create a new df with only year 2020 data

# Check the new columns with the df filtered to only year 2020 data
df_2020.head()
print()
df_2020.tail()
         date  lightning_strikes  week day_of_the_week # output
1  2020-07-19                416    29          Sunday
2  2020-05-11                462    20          Monday
7  2020-01-09                725     2        Thursday
8  2020-07-30                105    31        Thursday
9  2020-01-24                110     4          Friday

          date  lightning_strikes  week day_of_the_week
94  2020-06-05                575    23          Friday
96  2020-11-05                925    45        Thursday
97  2020-08-09                825    32          Sunday
98  2020-02-05                257     6       Wednesday
99  2020-06-21                155    25          Sunday

day_of_the_week_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] # defines the order of days for the box plot

# Create a box plot of strike totals per day of the week for the year 2020
g = sns.boxplot (data = df_2020,
                 x = 'day_of_the_week',
                 y = 'lightning_strikes',
                 order = day_of_the_week_order,
                 showfliers = True, # does include outliers
                )
g.set_title('Lightning distribution per day of the week (2020)')
plt.xlabel('Day of the week', labelpad = 20) # specifies the distance between the label and the corresponding axis
plt.ylabel('Number of lightning strikes', labelpad = 20)
plt.show()
