

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D') # create a range of dates from 2020-01-01 to 2024-12-31 ; generated on a daily frequency (each date in the range will be included)

sample_dates = np.random.choice(dates, size=100, replace=False) # randomly sample 100 unique dates from the 'dates' range
lightning_values = np.random.randint(100, 1000, size=len(dates))  # randomly generate 100 integers between 100 and 999

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

# Create 4 new columns
df['day'] = df['date'].dt.strftime('%d') # yyyy-mm-D##
df['week'] = df['date'].dt.strftime('%V') # yyyy-W##
df['month'] = df['date'].dt.strftime('%m') # yyyy-M##
df['quarter'] = df['date'].dt.to_period('Q').dt.strftime('%q') # yyyy-Q#
df['year'] = df['date'].dt.strftime('%Y') # yyyy

# Check the new columns
df.head()
print()
df.tail()
        date  lightning_strikes day week month quarter  year
0 2024-07-04                773  04   26    07      3  2024
1 2020-07-19                416  19   29    07      3  2020
2 2020-05-11                462  11   20    05      2  2020
3 2022-03-20                278  20   11    03      1  2022
4 2024-10-28                832  28   44    10      4  2024

95 2021-06-08                212  08   23    06      2  2021
96 2023-09-04                336  04   36    09      3  2023
97 2020-10-11                541  11   41    10      4  2020
98 2024-09-25                178  25   39    09      3  2024
99 2021-05-09                938  09   18    05      2  2021
