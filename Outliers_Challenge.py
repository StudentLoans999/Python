# TASK: 1. Create a df filled with yearly dates ranging from years 1900-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Add in a new column to the df that makes the number of lightning strikes more readable (since they are over 1 million per year)
# 3. Output the total mean and median of the lightning strikes
# 4. Create and plot a box plot (use sns and annotate each ) of: Lightning strikes per year (1900-2024)


# 3. Make another df that has the same date data to represent lightning strikes occurring but with these other columns: zip code, city, state, state code
# 4. Create a new df by merging the two dataframes together on columns 'date' and 'lightning_strikes'
# 5. Add in some null data to the new df to the columns 'longitude' and 'latitude' in randomly selected rows but make sure both columns don't have a missing value in the same row
# 6. Output the rows that contain missing values
# 7. Fill in the missing values by using the 'center_point_geom' column
# 8. Output the fully updated and fixed df that now doesn't have any missing values (verify that there aren't any missing values left)
# 9. Create and plot a geo graph (use plotly and annotate each data point in the plot) of: Lightning strikes per year (2020-2024) by City in the USA

#pip install matplotlib
#pip install pandas
#pip install seaborn
#pip install datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime

# Creates a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring, along with other columns
dates = pd.date_range(start='2000-01-01', end='2024-12-31', freq='Y') # create a range of dates from 2000-01-01 to 2024-12-31 ; generated on a yearly frequency (only one date per year in the range will be included)

sample_dates = np.random.choice(dates, size=100, replace=False) # randomly sample 100 unique dates from the 'dates' range
lightning_values = np.random.randint(1000, 50000001, size=len(sample_dates)) # randomly generate 100 integers between 1000 and 50000000

df = pd.DataFrame({'year': sample_dates, # create a DataFrame with 'sample_dates' as the values for a column 'year' and more columns
                   'lightning_strikes': lightning_values}
)
df
         year  lightning_strikes # output
0  1913-12-31           10230188
1  1991-12-31           17689058
2  1945-12-31           45735313
3  1999-12-31           37591262
4  1976-12-31           20411551
..        ...                ...
95 1949-12-31            7040521
96 1935-12-31            8859120
97 1911-12-31           39352798
98 1907-12-31           15107021
99 1963-12-31           13749411

def readable_numbers(x):
    """ Takes a large number and formats it into K (thousand) or M (million) to make it more readable """
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}K'.format(x*1e-3)
    return s

df['lightning_strikes_formatted'] = df['lightning_strikes'].apply(readable_numbers) # applies the function above to the 'lightning_strikes' column to create a new column 'lightning_strikes_formatted'
df
         year  lightning_strikes lightning_strikes_formatted # output
0  1995-12-31           24971455                       25.0M
1  1965-12-31           11811142                       11.8M
2  1988-12-31           43394227                       43.4M
3  1985-12-31             186265                        186K
4  1994-12-31           47375510                       47.4M
..        ...                ...                         ...
95 1901-12-31           46213098                       46.2M
96 1970-12-31           42197045                       42.2M
97 2023-12-31           31377902                       31.4M
98 2022-12-31           47874224                       47.9M
99 1947-12-31           14279968                       14.3M

# Gets the mean and median of the column 'lightning_strikes'
lightning_strikes_mean = readable_numbers(np.mean(df['lightning_strikes']))
lightning_strikes_median = readable_numbers(np.median(df['lightning_strikes']))
print(f"Mean: {lightning_strikes_mean}")
print(f"Median: {lightning_strikes_median}")
Mean: 25.2M # output
Median: 27.0M

# Create and plot a boxplot (with outliers shown)
box = sns.boxplot(x=df['lightning_strikes'], showfliers=True)
g = plt.gca()
ticks = g.get_xticks()
g.set_xticks(ticks)
g.set_xticklabels([readable_numbers(x) for x in ticks])
plt.xlabel('Number of strikes')
plt.title('Yearly number of lightning strikes (1900-2024)')
plt.show()
