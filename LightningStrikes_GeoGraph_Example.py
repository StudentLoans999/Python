# TASK: 1. Create a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Make the df have columns for geographic data: center_point, longitude, latitude
# 3. Make another df that has the same date data to represent lightning strikes occurring but with these other columns: zip code, city, state, state code
# 4. Create a new df by merging the two dataframes together on columns 'date' and 'lightning_strikes'
# 5. Add in some null data to the new df to the columns 'longitude' and 'latitude' but both columns can't have a missing value in the same row
# 6. Output the rows that contain missing values
# 7. Fill in the missing values by using the 'center_point_geom' column

# 3. Create a function to efficiently add a text label to a bar plot at specified positions (x, y), which will be implemented in bar charts later
# 4. Create and plot a bar chart of: weekly strike totals in 2020
# 5. Create and plot a bar chart of: quarterly strike totals in 2021-2022
# 6. Create and plot a bar chart (use sns and annotate each bar in the plot) of: yearly strike totals per quarter in 2020-2024

#pip install matplotlib
#pip install pandas
#pip install seaborn
#pip install datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime

# 
dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D') # create a range of dates from 2020-01-01 to 2024-12-31 ; generated on a daily frequency (each date in the range will be included)

sample_dates = np.random.choice(dates, size=100, replace=False) # randomly sample 100 unique dates from the 'dates' range
longitude = np.random.uniform(-180.0, 180.1, size=len(sample_dates)) # randomly generate 100 floats between -180 and 180
latitude = np.random.uniform(-90.0, 90.1, size=len(sample_dates)) # randomly generate 100 floats between -90 and 90
center_point_geom = df[['latitude', 'longitude']].mean(axis=1) # calculate the average latitude and longitude to get the center point
lightning_values = np.random.randint(100, 1000, size=len(sample_dates)) # randomly generate 100 integers between 100 and 999

df = pd.DataFrame({'date': sample_dates, # create a DataFrame with 'sample_dates' as the values for a column 'date' and more columns
                   'longitude': longitude,
                   'latitude': latitude,
                   'lightning_strikes': lightning_values})
# Calculate the average latitude and longitude to get the center point (with the format - POINT(longitude latitude) and then add it as a new column called 'center_point_geom'
df['center_point_geom'] = df.apply(lambda row: f"POINT({row['longitude']} {row['latitude']})", axis=1)

df = df.reindex(columns=['date', 'center_point_geom', 'longitude', 'latitude', 'lightning_strikes']) # reorder the columns so that 'center_point_geom' isn't at the end but right after 'date' instead 
df
         date    center_point_geom  longitude  latitude  lightning_strikes # output
0  2022-04-20  POINT(-132.4 -11.6)     -132.4     -11.6                802
1  2022-03-29    POINT(-50.2 54.7)      -50.2      54.7                517
2  2021-08-30   POINT(131.1 -82.3)      131.1     -82.3                378
3  2024-03-14    POINT(34.7 -33.3)       34.7     -33.3                654
4  2023-05-27     POINT(78.4 50.2)       78.4      50.2                835
..        ...                  ...        ...       ...                ...
95 2020-06-10    POINT(72.4 -87.3)       72.4     -87.3                221
96 2022-07-25   POINT(-141.0 82.9)     -141.0      82.9                854
97 2022-12-05    POINT(158.8 77.9)      158.8      77.9                616
98 2022-01-17     POINT(68.4 55.0)       68.4      55.0                627
99 2023-03-05   POINT(-104.3 83.5)     -104.3      83.5                167

df.shape # gets the shape of the df, which is 100 rows long and 5 columns wide 
(100, 5) # output

# Create a 'zip_code' column
zip_code = np.random.randint(100, 99950, size=len(sample_dates)) # randomly generate integers between 100 and the last zip code
zip_code = [str(code).zfill(5) for code in zip_code] # convert the zip codes to strings with leading zeros (since the first zip code is actually 00501) ; ensures that the first zip code has two leading zeros while the rest have leading zeros as needed to fill to five digits

# Create a list of USA cities and then randomly choose them 100 times to create the 'city' column (later on)
usa_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
          'Austin', 'Jacksonville', 'San Francisco', 'Indianapolis', 'Columbus', 'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'Washington',
          'Boston', 'El Paso', 'Nashville', 'Detroit', 'Oklahoma City', 'Portland', 'Las Vegas', 'Memphis', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque'
]
cities = np.random.choice(usa_cities, size=len(sample_dates))

# Create the corresponding states for each city
city_to_state = {
    "New York": "New York",
    "Los Angeles": "California",
    "Chicago": "Illinois",
    "Houston": "Texas",
    "Phoenix": "Arizona",
    "Philadelphia": "Pennsylvania",
    "San Antonio": "Texas",
    "San Diego": "California",
    "Dallas": "Texas",
    "San Jose": "California",
    "Austin": "Texas",
    "Jacksonville": "Florida",
    "San Francisco": "California",
    "Indianapolis": "Indiana",
    "Columbus": "Ohio",
    "Fort Worth": "Texas",
    "Charlotte": "North Carolina",
    "Seattle": "Washington",
    "Denver": "Colorado",
    "Washington": "District of Columbia",
    "Boston": "Massachusetts",
    "El Paso": "Texas",
    "Nashville": "Tennessee",
    "Detroit": "Michigan",
    "Oklahoma City": "Oklahoma",
    "Portland": "Oregon",
    "Las Vegas": "Nevada",
    "Memphis": "Tennessee",
    "Louisville": "Kentucky",
    "Baltimore": "Maryland",
    "Milwaukee": "Wisconsin",
    "Albuquerque": "New Mexico"
}
states = [city_to_state[city] for city in cities] # generate corresponding list of states for the randomly generated cities

# Create the corresponding state codes for each state
state_to_code = {
    "New York": "NY",
    "California": "CA",
    "Illinois": "IL",
    "Texas": "TX",
    "Arizona": "AZ",
    "Pennsylvania": "PA",
    "Florida": "FL",
    "Indiana": "IN",
    "Ohio": "OH",
    "North Carolina": "NC",
    "Washington": "WA",
    "Colorado": "CO",
    "District of Columbia": "DC",
    "Massachusetts": "MA",
    "Tennessee": "TN",
    "Michigan": "MI",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Nevada": "NV",
    "Kentucky": "KY",
    "Maryland": "MD",
    "Wisconsin": "WI",
    "New Mexico": "NM"
}
state_code = [state_to_code[state] for state in states]

df_zip = pd.DataFrame({'date': sample_dates, # create a new DataFrame with 'sample_dates' as the values for a column 'date' and more columns
                   'zip_code': zip_code,
                   'city': cities,
                   'state': states,
                   'state_code': state_code,
                   'lightning_strikes': lightning_values}
)
df_zip
         date zip_code          city       state state_code  lightning_strikes # output
0  2021-09-06    12393     Milwaukee   Wisconsin         WI                202
1  2024-10-16    69149  Indianapolis     Indiana         IN                723
2  2023-09-07    76791       Seattle  Washington         WA                731
3  2023-11-12    06819   Albuquerque  New Mexico         NM                481
4  2021-08-22    58903     Las Vegas      Nevada         NV                464
..        ...      ...           ...         ...        ...                ...
95 2020-12-19    17700  Jacksonville     Florida         FL                298
96 2020-01-18    03245    Fort Worth       Texas         TX                586
97 2020-11-25    16296    Louisville    Kentucky         KY                648
98 2020-07-08    77709       Detroit    Michigan         MI                495
99 2021-02-20    86350   Los Angeles  California         CA                399

print()
df_zip.shape
(100, 6) # output

# Merges 'df' to 'df_zip' to create a new df called 'df_joined' by using a left join on the columns 'date' and 'lightning_strikes'
df_joined = df.merge(df_zip, how='left', on=['date', 'lightning_strikes'])
df_joined
         date   center_point_geom  longitude  latitude  lightning_strikes zip_code           city       state state_code # output
0  2024-02-25    POINT(19.1 15.7)       19.1      15.7                927    93678         Denver    Colorado         CO
1  2021-10-21   POINT(39.4 -25.3)       39.4     -25.3                175    33833  Oklahoma City    Oklahoma         OK
2  2020-02-25   POINT(138.5 30.2)      138.5      30.2                109    17208     Fort Worth       Texas         TX
3  2024-11-14   POINT(97.8 -70.0)       97.8     -70.0                600    35272  San Francisco  California         CA
4  2023-08-16     POINT(62.5 5.6)       62.5       5.6                695    70335      Las Vegas      Nevada         NV
..        ...                 ...        ...       ...                ...      ...            ...         ...        ...
95 2022-01-19   POINT(-7.0 -35.7)       -7.0     -35.7                700    37886         Austin       Texas         TX
96 2024-12-05    POINT(-55.7 6.3)      -55.7       6.3                480    16807      San Diego  California         CA
97 2023-07-14  POINT(-128.8 20.4)     -128.8      20.4                798    69471   Indianapolis     Indiana         IN
98 2020-11-19    POINT(62.2 14.5)       62.2      14.5                775    02876     Louisville    Kentucky         KY
99 2021-08-06   POINT(47.7 -13.2)       47.7     -13.2                869    76298    San Antonio       Texas         TX

print()
df_joined.shape
(100, 9) # output

# Set some random entries in random rows to NaN in 'df_joined' (to create Null values)
num_null_rows = np.random.randint(1, min(len(df_joined.index) + 1, len(df_joined.columns) + 1)) # number of null values to introduce ; ensures num_null_rows is not greater than the number of rows nor columns, but is affecting at least 1 row

# Randomly choose between 'longitude' and 'latitude' columns for each null value, but only chooses either or per entry
for _ in range(num_null_rows): # iterates 'num_null_rows' times
    row_idx = np.random.choice(df_joined.index) # choose a random row index
    col_to_nullify = np.random.choice(['longitude', 'latitude']) # randomly choose between these two columns to set to NaN (but not both at the same time)
    df_joined.loc[row_idx, col_to_nullify] = np.nan # set the selected entry (location) to NaN

df_joined
         date    center_point_geom  longitude  latitude  lightning_strikes zip_code           city           state state_code # output
0  2022-12-10     POINT(34.8 40.2)       34.8      40.2                392    98434        El Paso           Texas         TX
1  2024-04-29     POINT(34.5 37.9)       34.5      37.9                891    82791         Denver        Colorado         CO
2  2022-04-22   POINT(-77.0 -59.2)      -77.0     -59.2                144    84858         Denver        Colorado         CO
3  2023-12-20  POINT(-146.4 -22.5)     -146.4     -22.5                913    73586        Phoenix         Arizona         AZ
4  2020-11-26    POINT(-63.2 38.6)      -63.2      38.6                868    00127      Nashville       Tennessee         TN
..        ...                  ...        ...       ...                ...      ...            ...             ...        ...
95 2023-11-05     POINT(74.4 40.8)       74.4      40.8                501    44870   Indianapolis         Indiana         IN
96 2023-07-02    POINT(-44.2 -2.9)      -44.2       NaN                350    80404  Oklahoma City        Oklahoma         OK
97 2021-10-06  POINT(-135.1 -51.0)     -135.1     -51.0                811    01734       Columbus            Ohio         OH
98 2022-06-07   POINT(-45.0 -56.2)      -45.0     -56.2                535    35465      Charlotte  North Carolina         NC
99 2021-03-24   POINT(-14.4 -59.2)      -14.4     -59.2                957    60530      Las Vegas          Nevada         NV
print()

df_joined.info()
<class 'pandas.core.frame.DataFrame'> # output
RangeIndex: 100 entries, 0 to 99
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   date               100 non-null    datetime64[ns]
 1   center_point_geom  100 non-null    object
 2   longitude          96 non-null     float64
 3   latitude           98 non-null     float64
 4   lightning_strikes  100 non-null    int32
 5   zip_code           100 non-null    object
 6   city               100 non-null    object
 7   state              100 non-null    object
 8   state_code         100 non-null    object
dtypes: datetime64[ns](1), float64(2), int32(1), object(5)
memory usage: 6.8+ KB
None

nan_rows = df_joined[df_joined.isnull().any(axis=1)] # contains only the rows (axis=1) where 'df_joined' has at least one NaN value
nan_rows
         date    center_point_geom  longitude  latitude  lightning_strikes zip_code           city                 state state_code # output
8  2020-12-07  POINT(-110.6 -48.2)        NaN     -48.2                150    07346     Washington  District of Columbia         DC
29 2021-08-18    POINT(-98.2 31.5)      -98.2       NaN                228    27887     Louisville              Kentucky         KY
36 2024-03-08     POINT(30.3 43.4)        NaN      43.4                148    20881  San Francisco            California         CA
44 2021-07-01    POINT(-37.9 63.2)        NaN      63.2                181    64663      Charlotte        North Carolina         NC
56 2024-12-11   POINT(-65.8 -35.0)        NaN     -35.0                116    09258         Boston         Massachusetts         MA
96 2023-07-02    POINT(-44.2 -2.9)      -44.2       NaN                350    80404  Oklahoma City              Oklahoma         OK
