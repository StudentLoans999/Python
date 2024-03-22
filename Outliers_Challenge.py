# TASK: 1. Create a df filled with yearly dates ranging from years 1900-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Add in a new column to the df that makes the number of lightning strikes more readable (since they are over 1 million per year)
# 3. Output the total mean and median of the lightning strikes
# 4. Create and plot a box plot (use sns) of: Lightning strikes per year (1900-2024)
# 5. Outliers aren't clear to see? Output the minimum and maximum lightning strikes value
# 6. Create 12 outliers for 12 random: one outlier is defined as having 0 lightning strikes, another is defined as having 100M, and then the other 10 are a random mix of low and high outliers 
# 7. Create and plot two bar charts (one for the low outliers and the other for high) (side-by-side) with the years sorted ascending (use plt and annotate each bar with the lightning value): Lightning strikes per year
# 8. Merge the original df with the df composed entirely of outliers
# 9. Output the new minimum and maximum lightning strikes value
# 10. Create and plot a box plot (use sns) showing the original df and with outliers pointed out (use a legend): Lightning strikes per year (1900-2024)
# 11. Output the 25th amd 75th percentile of annual strikes and the interquartile range, and the upper and lower limits
# 12. Delete any outliers that fall out of either the upper or lower range
# 13. Replace any outliers that fall out of the tenth_percentile or ninetieth_percentile to eitehr of those percentiles #
# 14. Reassign any outliers to be the median or mean value (show both but comment out the mean logic) 

#pip install matplotlib
#pip install pandas
#pip install seaborn
#pip install datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime
from matplotlib.lines import Line2D

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

print()

# Create and plot a boxplot (with outliers shown)
box = sns.boxplot(x=df['lightning_strikes'], showfliers=True)
g = plt.gca()
ticks = g.get_xticks()
g.set_xticks(ticks)
g.set_xticklabels([readable_numbers(x) for x in ticks])
plt.xlabel('Number of strikes')
plt.title('Yearly number of lightning strikes (1900-2024)')
plt.show()

# Gets the min and max values of the column 'lightning_strikes'
print("There don't seem to be any outliers present, so let's look at the Min and Max values and go from there")
print()
lightning_strikes_min = readable_numbers(np.min(df['lightning_strikes']))
lightning_strikes_max = readable_numbers(np.max(df['lightning_strikes']))
print(f"Min: {lightning_strikes_min}")
print(f"Max: {lightning_strikes_max}")
Min: 828K # output
Max: 49.6M

print()

# Generate 12 random years and 12 lightning strike values for outliers (one guranteed low at '1' and one guranteed high at '1M', and 10 random ones)
print("Let's add a low outlier (0), a high outlier (100M), and 10 random outliers")
print()
random_years_low_high = np.random.choice(dates, size=2) # generate random years for the lowest and highest outliers
random_years_10 = np.random.choice(dates, size=10) # generate random years for 10 outliers
random_strike_lowest = 0
random_strike_highest = 100000000 # 100 M
random_strike_10 = np.random.choice([1, 10, 50, 100, 500, 999, 50000000, 49999900, 49999000, 49998500], size=10)

outliers = pd.DataFrame({'year': np.concatenate((random_years_low_high, random_years_10)), # create a df for the 12 outliers
                         'lightning_strikes': [random_strike_lowest, random_strike_highest] + list(random_strike_10)})

print("Here are the outliers created:")
print()
outliers
         year  lightning_strikes # output
0  2009-12-31                  0
1  1970-12-31          100000000
2  1957-12-31                999
3  1929-12-31                100
4  1990-12-31           49999900
5  2007-12-31                999
6  1918-12-31                 50
7  1929-12-31                 50
8  2022-12-31                500
9  1910-12-31                500
10 1990-12-31                 50
11 1904-12-31                999

print()

# Create and plot two bar charts side-by-side: one for low outliers and the other for high #

outliers_df['year'] = outliers_df['year'].dt.strftime('%Y') # convert years to strings for plotting
outliers_df_sorted = outliers_df.sort_values(by = 'year', ascending = True) # sorts the years in ascending order

low_outliers = outliers_df_sorted[outliers_df_sorted['lightning_strikes'] < 1000]  # filter the low outliers
high_outliers = outliers_df_sorted[outliers_df_sorted['lightning_strikes'] >= 1000]  # filter the high outliers

low_outliers.reset_index(drop=True, inplace=True) # reset indicies of the low outliers
high_outliers.reset_index(drop=True, inplace=True) # reset indicies of the high outliers

# Function: Add text label to a bar plot at specified positions (x, y) for a given ax object
def add_labels_two_bars(ax, x, y, labels, format_labels=False):
    for i in range(len(x)):  # Iterate over the number of bars in the plot
        if format_labels: # if when function is called, it format_labels=True ; to be used for high outliers labels 
            formatted_label = readable_numbers(labels[i])
        else:
            formatted_label = labels[i]
        ax.text(x[i], y[i], formatted_label, ha='center', va='bottom', fontsize=12)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 5)) # 1 row and 2 columns of subplots (so side-by-side plots); 'fig' is the variable that holds a reference to the created figure; 'axs' is an array with 2 elements, each representing one of the subplots

# Plot low outliers as bars
low_bars = axs[0].bar(x=np.arange(len(low_outliers['year'])), height=low_outliers['lightning_strikes'], color='blue') # ax[0] is the first subplot so is low outliers ; x-axis is 'years'; positioning of the bars is evenly spaced values from 0 to len(years) ; height of the bars is 'lightning_strikes'
axs[0].set_title('Low Outliers')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Number of Lightning Strikes')
axs[0].set_xticks(np.arange(len(low_outliers['year']))) # sets the x-axis ticks based on the number of years ; each tick will correspond to a unique year from the low outliers' data, ensuring that each year is represented on the x-axis
axs[0].set_xticklabels(low_outliers['year'])

# Plot high outliers
high_bars = axs[1].bar(x=np.arange(len(high_outliers['year'])), height=high_outliers['lightning_strikes'], color='red') # ax[1] is the second subplot so is high outliers
axs[1].set_title('High Outliers')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Number of Lightning Strikes')
axs[1].set_xticks(np.arange(len(high_outliers['year'])))
axs[1].set_xticklabels(high_outliers['year'])
axs[1].set_ylim(0, 100000000) # set y-axis limit for the high outlier plot (to 100M)
axs[1].set_yticklabels([readable_numbers(x) for x in axs[1].get_yticks()]) # format y-axis ticks using the readable_numbers function (makes them M)

# Add labels to the top of each bar using the add_labels function
add_labels_two_bars(axs[0], np.arange(len(low_outliers['year'])), low_outliers['lightning_strikes'], low_outliers['lightning_strikes']) # adds labels to lower outlier's bars, each label is a year and its corresponding 'lightning_strikes' value 
add_labels_two_bars(axs[1], np.arange(len(high_outliers['year'])), high_outliers['lightning_strikes'], high_outliers['lightning_strikes'], format_labels=True) # makes the label in the format of having 'M'

plt.tight_layout() # automatically adjusts the subplots' parameters so that the subplots fit nicely
plt.show()
# #


df_with_outliers = pd.concat([df, outliers_df], ignore_index=True) # merges 'outliers' df to the original df 'df'

# Gets the new min and max values of the column 'lightning_strikes'
lightning_strikes_min = readable_numbers(np.min(df_with_outliers['lightning_strikes']))
lightning_strikes_max = readable_numbers(np.max(df_with_outliers['lightning_strikes']))
print("Here are the new Min and Max values:")
print(f"Min: {lightning_strikes_min}")
print(f"Max: {lightning_strikes_max}")
Here are the new Min and Max values: # output
Min: 0K
Max: 100.0M

print()

# Create and plot a box plot with all the data and then overlay the outliers to it #

combined_plot = sns.boxplot(x=df_with_outliers['lightning_strikes']) # creates a box plot
sns.stripplot(x=outliers_df['lightning_strikes'], color='red', jitter=True) # create a strip plot of just the outliers

# Increase x-axis range for better spread 
x_min, x_max = plt.gca().get_xlim() # retrieves the current limits of the x-axis
buffer = 0.2 * (x_max - x_min)  # calculates the buffer size, which is 20% of the range of the x-axis data
new_min = x_min - buffer
new_max = x_max + buffer
plt.xlim(new_min, new_max) # sets the new limits for the x-axis

plt.xlabel('Number of strikes')
plt.title('Yearly number of lightning strikes (1900-2024)')

legend_elements = [ # add legend with custom markers
    Line2D([0], [0], color='b', lw=2, label='Data'), # creates a line with zero length (essentially a point) and a width of 2
    Line2D([0], [0], marker='o', color='w', label='Outliers', markerfacecolor='red', markersize=10) # reates a line with zero length (essentially a point) represented by a circle marker
]
plt.legend(handles=legend_elements) # creates a legend with the custom markers above

# X-axis ticks remain at their current positions while updating the tick labels to be more readable
g = plt.gca() # gets the current axes instance from the current figure
ticks = g.get_xticks() # retrieves the current positions of the x-axis ticks on the plot
g.set_xticks(ticks) # ensures that the ticks remain at the same positions
g.set_xticklabels([readable_numbers(x) for x in ticks]) # makes each tick position 'x' more readable (M)

plt.show()
# #


percentile25 = df_with_outliers['lightning_strikes'].quantile(0.25) # calculate 25th percentile of annual strikes
percentile75 = df['lightning_strikes'].quantile(0.75) # calculate 75th percentile of annual strikes

iqr = percentile75 - percentile25 # calculate interquartile range

upper_limit = percentile75 + 1.5 * iqr # calculate upper and lower thresholds for outliers
lower_limit = percentile25 - 1.5 * iqr
print('25th percentile of annual strikes is: ', readable_numbers(percentile25))
print('75th percentile of annual strikes is: ', readable_numbers(percentile75))
print('Interquartile range is: ', readable_numbers(iqr))
print('Upper limit is: ', readable_numbers(upper_limit))
print('Lower limit is: ', readable_numbers(lower_limit))
25th percentile of annual strikes is: 7.5M # output
75th percentile of annual strikes is: 33.6M
Interquartile range is:  26.1M
Upper limit is:  72.8M
Lower limit is:  -31634K
# Delete any outliers that fall out of either the upper or lower range #
mask = (df_with_outliers['lightning_strikes'] >= lower_limit) & (df_with_outliers['lightning_strikes'] <= upper_limit)

mask = mask.reindex(df_with_outliers.index) # ensure that 'mask' has the same index as 'df_with_outliers'
df_with_outliers_removed = df_with_outliers[mask].copy()
df_with_outliers_removed
                    year  lightning_strikes lightning_strikes_formatted # output
0    2020-12-31 00:00:00           44560188                       44.6M
1    1980-12-31 00:00:00           35696891                       35.7M
2    1920-12-31 00:00:00           45239799                       45.2M
3    1975-12-31 00:00:00           32304632                       32.3M
4    1939-12-31 00:00:00            3044779                        3.0M
..                   ...                ...                         ...
107                 1919           50000000                         NaN
108                 1904           49999000                         NaN
109                 1987                500                         NaN
110                 2004           49999900                         NaN
111                 1992                 10                         NaN

# #


# Replace any outliers that fall out of the tenth_percentile or ninetieth_percentile to eitehr of those percentiles #
tenth_percentile = np.percentile(df_with_outliers['lightning_strikes'], 10) # calculate 10th percentile
ninetieth_percentile = np.percentile(df_with_outliers['lightning_strikes'], 90) # calculate 90th percentile

# Apply lambda function to replace outliers with thresholds defined above
df_with_outliers['lightning_strikes'] = df_with_outliers['lightning_strikes'].apply(lambda x: (
    tenth_percentile if x < tenth_percentile # set x to tenth_percentile if it is less than tenth_percentile
    else ninetieth_percentile if x > ninetieth_percentile # set x to ninetieth_percentile if it is more than ninetieth_percentile
    else x)) # set x to x if it falls within the percentiles (think of them as walls)

df_with_outliers['lightning_strikes']
0      44560188.0 # output
1      35696891.0
2      45239799.0
3      32304632.0
4       3044779.0
          ...
107    47258765.6
108    47258765.6
109      953084.2
110    47258765.6
111      953084.2
Name: lightning_strikes, Length: 112, dtype: float64

print()                 
# #


# Calculate the median and then impute it for all outliers that fall out of either the upper or lower range #
median = np.median(df_with_outliers['lightning_strikes'][(df_with_outliers['lightning_strikes'] >= lower_limit) & (df_with_outliers['lightning_strikes'] <= upper_limit)]) # calculates the median based on non-outlier values only (values that fall within the lower and upper limits)
df_with_outliers['lightning_strikes'] = np.where(df_with_outliers['lightning_strikes'] < lower_limit, median, df_with_outliers['lightning_strikes']) # impute the median for all values < lower_limit
df_with_outliers['lightning_strikes'] = np.where(df_with_outliers['lightning_strikes'] > upper_limit, median, df_with_outliers['lightning_strikes']) # impute the median for all values > upper_limit
df_with_outliers['lightning_strikes']
0       1213451.8 # output
1      32963531.0
2      33849901.0
3      18152930.0
4       3718059.0
          ...
107     1213451.8
108     1213451.8
109     1213451.8
110     1213451.8
111    46048771.4
Name: lightning_strikes, Length: 112, dtype: float64

# Calculate the mean and then impute it for all outliers that fall out of either the upper or lower range
mean = np.mean(df_with_outliers['lightning_strikes'][(df_with_outliers['lightning_strikes'] >= lower_limit) & (df_with_outliers['lightning_strikes'] <= upper_limit)]) # calculates the mean based on non-outlier values only (values that fall within the lower and upper limits)
df_with_outliers['lightning_strikes'] = np.where(df_with_outliers['lightning_strikes'] < lower_limit, mean, df_with_outliers['lightning_strikes']) # impute the mean for all values < lower_limit
df_with_outliers['lightning_strikes'] = np.where(df_with_outliers['lightning_strikes'] > upper_limit, mean, df_with_outliers['lightning_strikes']) # impute the mean for all values > upper_limit
#df_with_outliers['lightning_strikes'] # uncomment this line if you want to see the output
