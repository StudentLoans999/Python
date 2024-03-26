# TASK: 1. Create a df filled with daily dates ranging from years 1900-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Add in a new column to the df to represent the months for each date (categorical and in order) to represent lightning strikes occurring
# 3. Filter and output rows where there are actually lightning strikes occurring on that date
# 4. Create a categorical variable by bucketing the number of lightning strikes per month into severeness levels based on quantiles
# 5. Create dummy variables from strike levels ('0/False' where is absent and '1/True' where present) and add them to the df
# 6. Create and plot a heatmap (use sns) showing monthly lightning severity over the years

# Label Encoding - A data transformation technique where each data value is assigned a distinct number instead of a qualitative value EX: ['Scattered', 'Mild', 'Heavy', 'Severe'] transforms to [0, 1, 2, 3] #

#pip install matplotlib
#pip install pandas
#pip install seaborn
#pip install datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime

# Creates a df filled with daily dates ranging from years 1900-2024 and assign random values for each date to represent lightning strikes occurring, along with other columns
dates = pd.date_range(start='2000-01-01', end='2024-12-31', freq='D') # create a range of dates from 2000-01-01 to 2024-12-31 ; generated on a daily frequency

sample_dates = np.random.choice(dates, size=100, replace=False) # randomly sample 100 unique dates from the 'dates' range
lightning_values = np.random.randint(1000, 50000001, size=len(sample_dates)) # randomly generate 100 integers between 1000 and 50000000

df = pd.DataFrame({'date': sample_dates, # create a DataFrame with 'sample_dates' as the values for a column 'date' and more columns
                   'lightning_strikes': lightning_values}
)
df
         date  lightning_strikes # output
0  2014-02-25           16359758
1  2022-09-09           37798968
2  2001-02-09           44300816
3  2006-11-19            6415402
4  2018-09-06           26540489
..        ...                ...
95 2004-05-02           27116728
96 2005-08-03           43783303
97 2002-08-20           31115237
98 2015-04-28           18837405
99 2017-03-16           11651788

print()

# Create a 'year' column; Create a 'month' column and makes the names categorical and in order
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month_name().str.slice(stop=3)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['month'] = pd.Categorical(df['month'], categories=months, ordered=True)

df_by_month = df.groupby(['year', 'month']).agg({'date': 'first', 'lightning_strikes': 'sum'}).reset_index() # group by 'year' and 'month' and sum the lightning strikes
df_by_month = df_by_month[['date', 'month', 'year', 'lightning_strikes']] # reorder the columns
df_by_month
          date month  year  lightning_strikes
0   2000-01-13   Jan  2000           47946394
1          NaT   Feb  2000                  0
2   2000-03-09   Mar  2000           30615784
3          NaT   Apr  2000                  0
4          NaT   May  2000                  0
..         ...   ...   ...                ...
295 2024-08-07   Aug  2024           10184669
296        NaT   Sep  2024                  0
297 2024-10-04   Oct  2024           63699273
298 2024-11-20   Nov  2024           17922375
299        NaT   Dec  2024                  0

print()

# Filter rows where lightning_strikes is greater than 0
df_lightning = df_by_month[df_by_month['lightning_strikes'] > 0]
print(df_lightning)
          date month  year  lightning_strikes # output
0   2000-01-13   Jan  2000           47946394
2   2000-03-09   Mar  2000           30615784
7   2000-08-18   Aug  2000           18565290
9   2000-10-30   Oct  2000           24304341
10  2000-11-22   Nov  2000           43422619
..         ...   ...   ...                ...
278 2023-03-25   Mar  2023           16106294
282 2023-07-27   Jul  2023           61587629
295 2024-08-07   Aug  2024           10184669
297 2024-10-04   Oct  2024           63699273
298 2024-11-20   Nov  2024           17922375

print()

# Create a categorical variable by bucketing the number of lightning strikes per month into severeness levels based on quantiles
df_by_month = df_by_month.drop_duplicates(subset=['lightning_strikes']) # drop duplicate rows based on 'lightning_strikes'
df_by_month['strike_level'] = pd.qcut(df_by_month['lightning_strikes'], 4, labels = ['Scattered', 'Mild', 'Heavy', 'Severe'])
print(df_by_month)
          date month  year  lightning_strikes strike_level # output
0          NaT   Jan  2000                  0    Scattered
1   2000-02-05   Feb  2000            8987753    Scattered
4   2000-05-18   May  2000           26889752         Mild
5   2000-06-23   Jun  2000            8218302    Scattered
7   2000-08-11   Aug  2000            1732617    Scattered
..         ...   ...   ...                ...          ...
281 2023-06-12   Jun  2023           38856030        Heavy
283 2023-08-01   Aug  2023            9810531    Scattered
289 2024-02-26   Feb  2024           41308201        Heavy
292 2024-05-21   May  2024           13616841    Scattered
299 2024-12-10   Dec  2024           14427200    Scattered

print()

df_by_month['strike_level_code'] = df_by_month['strike_level'].cat.codes # assign numerical values to the strike levels
print(df_by_month)
          date month  year  lightning_strikes strike_level  strike_level_code # output
0          NaT   Jan  2000                  0    Scattered                  0
2   2000-03-24   Mar  2000           34335930        Heavy                  2
7   2000-08-22   Aug  2000           29312046         Mild                  1
10  2000-11-06   Nov  2000           44822963       Severe                  3
12  2001-01-01   Jan  2001           17433009    Scattered                  0
..         ...   ...   ...                ...          ...                ...
279 2023-04-26   Apr  2023           68950610       Severe                  3
284 2023-09-20   Sep  2023           35837758        Heavy                  2
286 2023-11-14   Nov  2023           36585246        Heavy                  2
297 2024-10-15   Oct  2024           29647930        Heavy                  2
299 2024-12-27   Dec  2024           77267173       Severe                  3

print()

# Create dummy variables from strike levels ('0/False' where is absent and '1/True' where present) and add to df
dummy_vars = pd.get_dummies(df_by_month['strike_level'])
df_by_month = pd.concat([df_by_month, dummy_vars], axis=1) # concat along the columns (aligns df side-by-side)
df_by_month
          date month  year  lightning_strikes strike_level  strike_level_code  Scattered   Mild  Heavy  Severe # output
0          NaT   Jan  2000                  0    Scattered                  0       True  False  False   False
2   2000-03-03   Mar  2000            9857964    Scattered                  0       True  False  False   False
10  2000-11-22   Nov  2000            6922408    Scattered                  0       True  False  False   False
22  2001-11-23   Nov  2001           47005384       Severe                  3      False  False  False    True
24  2002-01-09   Jan  2002            1169484    Scattered                  0       True  False  False   False
..         ...   ...   ...                ...          ...                ...        ...    ...    ...     ...
277 2023-02-02   Feb  2023           42389586       Severe                  3      False  False  False    True
278 2023-03-06   Mar  2023           33712256        Heavy                  2      False  False   True   False
279 2023-04-15   Apr  2023           33278091        Heavy                  2      False  False   True   False
282 2023-07-11   Jul  2023           42573909       Severe                  3      False  False  False    True
292 2024-05-27   May  2024          119740261       Severe                  3      False  False  False    True
           
print()

df_by_month_plot = df_by_month.pivot(index='year', columns='month', values='strike_level_code').fillna(0).astype(int) # format df indices to prepare for plotting' makes 'NaN' values as '0' and the rest as ints 
df_by_month_plot
month  Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec # output
year
2000     0    0    0    0    0    3    0    2    1    0    0    0
2001     1    0    0    1    0    0    0    0    0    0    3    0
2002     1    0    0    0    0    0    0    0    1    3    0    0
2003     1    0    0    0    0    0    0    1    0    0    0    0
2004     0    0    0    3    3    0    0    0    2    2    0    0
2005     0    2    1    1    0    0    0    3    0    0    0    0
2006     0    0    0    2    0    0    0    0    0    0    1    0
2007     0    2    0    0    0    0    0    0    0    2    0    0
2008     0    0    0    0    0    0    3    0    0    0    0    0
2009     0    0    0    0    0    0    0    0    2    0    3    0
2010     0    0    0    0    0    0    0    0    0    0    0    0
2011     0    0    0    0    1    0    0    0    1    0    0    0
2012     0    0    1    0    0    0    0    0    0    0    3    2
2013     0    0    0    0    0    0    0    0    2    0    3    0
2014     0    0    0    0    0    3    3    3    0    0    0    0
2015     0    0    0    0    0    0    0    0    0    0    0    0
2016     0    0    0    0    0    0    0    0    2    1    0    0
2017     1    0    0    0    0    0    0    0    1    0    3    3
2018     0    0    2    0    0    2    2    3    0    0    1    0
2019     0    2    0    0    0    0    2    0    0    0    0    3
2020     0    0    0    0    2    0    0    3    0    0    0    0
2022     1    0    0    0    0    0    0    2    0    0    0    3
2023     1    0    0    2    1    0    0    0    0    0    0    0
2024     2    0    0    3    0    2    1    0    0    0    3    0

print()

# Create and plot a heatmap showing which months over the years had the most severe lightning
ax = sns.heatmap(df_by_month_plot, cmap = 'Reds') # create heatmap with 'df_by_month_plot' data by color 'Red'
colorbar = ax.collections[0].colorbar # access the colorbar
colorbar.set_ticks([0, 1, 2, 3]) # sets the tick positions on the colorbar corresponding to the categories of lightning severity (listed below)
colorbar.set_ticklabels(['Scattered', 'Mild', 'Heavy', 'Severe'])
plt.xlabel('Month')
plt.ylabel('Year')
plt.title("Monthly Lightning strikes' Intensity over Years (2000-2024)")
ax.hlines(np.arange(len(df_by_month_plot.index)) + 0.07, * ax.get_xlim(), colors = 'black', linewidth = 0.5) # add horizontal lines between each row (year)
ax.vlines(np.arange(len(df_by_month_plot.columns)) + 0.006, * ax.get_ylim(), colors = 'black', linewidth = 0.5) # add vertical lines between each column (month)
plt.gca().invert_yaxis() # inverts the y-axis (so that the bottom starts with year 2000)
plt.show()
