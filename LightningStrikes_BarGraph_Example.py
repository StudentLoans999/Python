
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

# Add text label to a bar plot at specified positions (x, y) 
def add_labels(x, y, labels):
    for i in range(len(x)): #  iterates over the number of bars in the plot
        plt.text(i, y[i], labels[i], ha = 'center', va = 'bottom') # 'i' is index of the data point (horizontal position); 'y[i]' is value of the data point at the current index (vertical position)

df_by_week_2020 = df[df['year'] == '2020'].groupby('week')['lightning_strikes'].sum().reset_index() # create new df view of just 2020 lightning_strikes data, summed by week
df_by_week_2020
   week  lightning_strikes # output
0    11                904
1    14               1072
2    16               1396
3    17                300
4    31                181
5    38               2385
6    40                305
7    41                341
8    42               1334
9    43               1629
10   47                351
11   49                905
12   50                898

# Plot a bar chart of weekly strike totals in 2020
plt.figure(figsize = (20, 5)) # increase output size
plt.bar(x=df_by_week_2020['week'], height=df_by_week_2020['lightning_strikes']) # create a bar chart showing lightning strikes by weeks
plt.xlabel("Week number") # x-axis title
plt.ylabel("Number of lightning strikes") # y-axis title
add_labels(df_by_week_2020['week'], df_by_week_2020['lightning_strikes'], df_by_week_2020['lightning_strikes'])  # labels the number of lightning strikes on top of the bar
plt.title("Number of lightning strikes per week (2020)") # title
plt.xticks(rotation = 45, fontsize = 10) # rotate x-axis labels and decrease font size
plt.plot() # create a plot
plt.show() # shows the created bar chart

df_by_quarter_2021_2022 = df[(df['year'].isin(['2021', '2022']))].groupby(['year', 'quarter'])['lightning_strikes'].sum().reset_index() # create new df view of just 2021 and 2022 lightning_strikes data (have to reset index for bar chart to work), summed by quarter
df_by_quarter_2021_2022
year  quarter # output if .reset_index() is removed
2021  1          3104
      2          3150
      3          1077
      4          1105
2022  1           946
      2          4480
      3          4956
      4          1312
Name: lightning_strikes, dtype: int32

quarters = 'Q' +  df_by_quarter_2021_2022['quarter'] + ' ' + df_by_quarter_2021_2022['year']  # concatenate 'quarter' and 'year' columns

plt.figure(figsize = (15, 5)) # increase output size
plt.bar(x = quarters, height = df_by_quarter_2021_2022['lightning_strikes']) # create a bar chart showing lightning strikes by quarters
plt.xlabel("Quarter") # x-axis title
plt.ylabel("Number of lightning strikes") # y-axis title
add_labels(df_by_quarter_2021_2022['quarter'], df_by_quarter_2021_2022['lightning_strikes'], df_by_quarter_2021_2022['lightning_strikes']) # labels the number of lightning strikes on top of the bar
plt.title("Number of lightning strikes per quarter (2021-2022)") # title
plt.plot() # create a plot
plt.show() # shows the created bar chart

# Create a new df
df_by_quarter_2020_2021_2022_2023_2024 = df[df['year'].isin(['2020', '2021', '2022', '2023', '2024'])].groupby(['year', 'quarter'])['lightning_strikes'].sum().reset_index() # create new df view of all the years of lightning_strikes data summed by quarter

# Create 2 new columns from the newly created df
df_by_quarter_2020_2021_2022_2023_2024['quarter_number'] = df_by_quarter_2020_2021_2022_2023_2024['quarter'].astype(int)
df_by_quarter_2020_2021_2022_2023_2024['year'] = df_by_quarter_2020_2021_2022_2023_2024['year'].astype(int)
df_by_quarter_2020_2021_2022_2023_2024

plt.figure(figsize = (15, 5))
p = sns.barplot(
    data = df_by_quarter_2020_2021_2022_2023_2024,
    x = 'quarter_number',
    y = 'lightning_strikes',
    hue = 'year'
)
for b in p.patches:
    p.annotate(str(round(b.get_height()/1000000, 1)) + 'M',
               (b.get_x() + b.get_width() / 2., b.get_height() + 1.2e6),
               ha = 'center', va = 'bottom',
               xytext = (0, -12),
               textcoords = 'offset points'
    )
plt.xlabel("Quarter") # x-axis title
plt.ylabel("Number of lightning strikes") # y-axis title


#Annotate each bar with its value

for index, row in df_by_quarter_2020_2021_2022_2023_2024.iterrows():
    if row['year'] == 2020:
        x_pos = row['quarter_number'] + (int(row['year']) - 2024) * 0.33
    elif row['year'] == 2021:
        x_pos = row['quarter_number'] + (int(row['year']) - 2023) * 0.58
    elif row['year'] == 2022:
        x_pos = row['quarter_number'] + (int(row['year']) - 2022) * 0.33
    elif row['year'] == 2023:
        x_pos = row['quarter_number'] + (int(row['year']) - 2021) * 0.33
    elif row['year'] == 2024:
        x_pos = row['quarter_number'] + (int(row['year']) - 2020) * 0.33

    y_pos = row['lightning_strikes']  # Use the lightning strike value as y-coordinate
    p.text(x_pos, y_pos, str(row['lightning_strikes']), 
           color='black', ha='center', va='bottom')

plt.title("Number of lightning strikes per quarter (2020-2024)") # title
plt.show() # shows the created bar chart
