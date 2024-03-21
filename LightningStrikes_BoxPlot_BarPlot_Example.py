# TASK: 1. Create a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Make the df have columns for the week number in the year and the day of the week
# 3. Filter the df to only have year 2020 data in it 
# 4. Create and plot a box plot (use sns) of: strike totals per day of the week for the year 2020
# 5. Combine the filtered year 2020 data with year 2024 data, but remove the week number and day of the week columns first
# 6. Output the two years' total lightning strikes, with the year of least lightning strikes first
# 7. Output (in bold) which year of those two had the least lightning strikes and the number of strikes
# 8. Calculate total lightning strikes for each month of each year (2020-2024)
# 9. Calculate total lightning strikes for each year (2020-2024)
# 10. Create and plot a bar chart (use sns) of: the percentage of lightning strikes each month for each year (2020-2024)

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

# Iterate over each box in the plot and annotate: height is above the top of the box; width is centered
for b in g.artists: # iterates over each box in the box plot (each box is represented as a patch object)
  bbox = b.get_bbox()  # get the bounding box of the box
  y_pos_upper = bbox.y1 + 0.2e6  # add a little offset above the top of the box
  y_pos_lower = bbox.y0 - 0.2e6  # subtract a slightly offset below the bottom of the box
  
  # Annotate upper bound each box
  g.annotate(str(round(bbox.y1, 1)), # adds text annotations to the upper bound of each box. Rounds the upper bound of the box to one decimal place and then converts it to a string 
              (bbox.x0 + bbox.width / 2, y_pos_upper), # places the annotation at the center of the box horizontally and slightly above the top of the box
              ha = 'center', va = 'bottom', # sets horizontal alignment to center and vertical alignment to the bottom
              xytext = (0, 6), # offsets the current position zero units horizontally and twelve units down
              textcoords = 'offset points' # indicates that the xytext coordinates are interpreted as offset points from the xy coordinates
  )

# Annotate each box with its value
for index, row in df_2020.iterrows(): # iterates over each row in the df
  x_pos = row['day_of_the_week']
  y_pos = row['lightning_strikes']  # uses the lightning strike value as y-coordinate
  g.text(x_pos, y_pos, str(row['lightning_strikes']), # adds a text annotation to the plot. 'lightning_strikes' value is converted to a string and is displayed as the annotation
           color = 'red', ha = 'center', va = 'bottom') # color and positioning of the text
  
g.set_title('Lightning distribution per day of the week (2020)')
plt.xlabel('Day of the week', labelpad = 20) # specifies the distance between the label and the corresponding axis
plt.ylabel('Number of lightning strikes', labelpad = 20)
plt.show()

# Combine the filtered year 2020 data with year 2024 data, after removing the 'week' and 'day_of_the_week' columns
df_2024 = df[df['date'].dt.year == 2024] # create a new df with only year 2024 data
df_2020 = df_2020.drop(['week', 'day_of_the_week'], axis = 1) # drop 'week' and 'day_of_the_week' columns from year 2020 data
df_2024 = df_2024.drop(['week', 'day_of_the_week'], axis = 1)  # drop 'week' and 'day_of_the_week' columns from year 2024 data
df_2020_2024 = pd.concat([df_2020, df_2024], ignore_index = True) # join year 2020 data to year 2024 data without 'week' and 'day_of_the_week'

df_2020_2024.head()
print()
df_2020_2024.tail()
        date  lightning_strikes # output
0 2020-06-26                450
1 2020-01-07                629
2 2020-01-15                512
3 2020-08-14                960
4 2020-06-13                643

         date  lightning_strikes
29 2024-10-07                587
30 2024-03-06                841
31 2024-07-14                423
32 2024-07-26                408
33 2024-10-16                443

# Lists first which year (2020 or 2024) had the least lightning strikes
df_2020_2024['year'] = df_2020_2024['date'].dt.strftime('%Y') # makes a 'year' column in this format: yyyy
total_lightning_strikes_by_year = df_2020_2024[['year', 'lightning_strikes']].groupby(['year']).sum() # groups the total lightning strikes by year
total_lightning_strikes_by_year_sorted = total_lightning_strikes_by_year.sort_values(by = 'lightning_strikes', ascending = True)

total_lightning_strikes_by_year_sorted
      lightning_strikes # output
year
2024               7909
2020               9293


# Output the year with the least lightning strikes and the number of strikes
year_least_strikes = total_lightning_strikes_by_year_sorted.index[0] # get the first row's column (the year with the least strikes)
lightning_strikes_least = total_lightning_strikes_by_year_sorted.loc[year_least_strikes, 'lightning_strikes'] # get the value in the row with the least strikes and in the 'lightning_strikes' column
print(f"The year with the least lightning strikes is \033[1m{year_least_strikes}\033[0m with \033[1m{lightning_strikes_least}\033[0m strikes")

# Calculate total lightning strikes for each month of each year (2020-2024)
df['month'] = df['date'].dt.strftime('%m') # makes a 'month' column in this format: yyyy-MM
df['year'] = df['date'].dt.strftime('%Y') # makes a 'year' column in this format: yyyy

lightning_by_month = df.groupby(['month', 'year']).agg( # group df by 'month' and 'year' and aggregate the sums of 'lightning_strikes' into a new column called 'number_of_strikes'
  number_of_strikes = ('lightning_strikes', 'sum')
  ).reset_index()

lightning_by_month.head()
print()
lightning_by_month.tail()
  month  year  number_of_strikes # output
0    01  2020               1915
1    01  2021               2024
2    01  2022                116
3    01  2023               1953
4    01  2024               1300

   month  year  number_of_strikes
45    11  2024                697
46    12  2021               2973
47    12  2022                175
48    12  2023                564
49    12  2024                344

# Calculate total lightning strikes for each month of each year (2020-2024)
df['month'] = df['date'].dt.strftime('%m') # makes a 'month' column in this format: yyyy-MM
df['year'] = df['date'].dt.strftime('%Y') # makes a 'year' column in this format: yyyy

lightning_by_month = df.groupby(['month', 'year']).agg( # group df by 'month' and 'year' and aggregate the sums of 'lightning_strikes' into a new column called 'number_of_strikes'
  number_of_strikes = ('lightning_strikes', 'sum')
  ).reset_index()

lightning_by_month.head()
print()
lightning_by_month.tail()
  month  year  monthly_strikes # output
0    01  2020               1915
1    01  2021               2024
2    01  2022                116
3    01  2023               1953
4    01  2024               1300

   month  year  monthly_strikes
45    11  2024                697
46    12  2021               2973
47    12  2022                175
48    12  2023                564
49    12  2024                344

# Calculate total lightning strikes for each year (2020-2024)
lightning_by_year = df.groupby(['year']).agg( # group df by 'year' and aggregate the sums of 'lightning_strikes' into a new column called 'yearly_strikes'
  yearly_strikes = ('lightning_strikes', 'sum')
  ).reset_index()

lightning_by_year.head()
   year  yearly_strikes # output
0  2020            8694
1  2021           10152
2  2022           10241
3  2023            8860
4  2024           15741

# Create a bar chart of the percentage of lightning strikes each month for each year (2020-2024)
percentage_lightning = lightning_by_month.merge(lightning_by_year, on = 'year') # merge the 'lightning_by_month' df with the 'lightning_by_year' df on the shared key 'year'
percentage_lightning.head()
  month  year  monthly_strikes  yearly_strikes # output
0    01  2020              919            9935
1    01  2021             2410           13284
2    01  2022              415            9406
3    01  2024             1062           10734
4    02  2020              977            9935

percentage_lightning['percentage_lightning_per_month'] = round((percentage_lightning.monthly_strikes / percentage_lightning.yearly_strikes * 100), 1) # makes a new column called 'percentage_lightning_per_month' that is 'monthly_strikes' / 'yearly_strikes' * 100 and rounded to one decimal place
percentage_lightning.head()
print()
percentage_lightning.tail()
  month  year  monthly_strikes  yearly_strikes  percentage_lightning_per_month # output
0    01  2020              919            9935                             9.3
1    01  2021             2410           13284                            18.1
2    01  2022              415            9406                             4.4
3    01  2024             1062           10734                             9.9
4    02  2020              977            9935                             9.8

   month  year  monthly_strikes  yearly_strikes  percentage_lightning_per_month
45    11  2022              879            9406                             9.3
46    11  2023              805           12532                             6.4
47    11  2024              831           10734                             7.7
48    12  2022             1040            9406                            11.1
49    12  2024             1405           10734                            13.1

percentage_lightning['month'] = df['date'].dt.strftime('%B') # changes the 'month' column to be the full name of the month, instead of just the number
percentage_lightning
      month  year  monthly_strikes  yearly_strikes  percentage_lightning_per_month # output
0   January  2020             2291            9915                            23.1
1      June  2022             2067           14943                            13.8
2  December  2023              724           10261                             7.1
3       May  2024              699           10522                             6.6
4      June  2022              780           14943                             5.2

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] # defines the order of months for the bar chart

# Function: Add text label to a bar plot at specified positions (x, y) 
def add_labels(x, y, labels):
    for i in range(len(x)): #  iterates over the number of bars in the plot
        plt.text(i, y[i], labels[i], ha = 'center', va = 'bottom') # 'i' is index of the data point (horizontal position); 'y[i]' is value of the data point at the current index (vertical position)

plt.figure(figsize = (10, 6)) # increase output size
sns.barplot(
  data = percentage_lightning,
  x = 'month',
  y = 'percentage_lightning_per_month',
  hue = 'year',
  order = month_order
) # creates a bar chart with data from 'percentage_lightning' df
plt.xlabel("Month", labelpad = 20) # specifies the distance between the label and the corresponding axis
plt.ylabel("% of lightning strikes", labelpad = 20)

formatted_labels = [f"{value}%" for value in percentage_lightning['percentage_lightning_per_month']] # convert numerical values to strings and concatenate '%' to each value (so can add percent sign to the value's label)
add_labels(percentage_lightning['month'], percentage_lightning['percentage_lightning_per_month'], formatted_labels)  # labels the percentage of lightning strikes per month on top of the bar
plt.title("% of lightning strikes each Month (2020-2024)")
plt.show()
