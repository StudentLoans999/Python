# TASK: 1. Create a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Make the df have columns for geographic data: center_point, longitude, latitude
# 3. Make another df that has the same date data to represent lightning strikes occurring but with these other columns: zip code, city, state, state code
# 4. Create a new df by merging the two dataframes together on columns 'date' and 'lightning_strikes'
# 5. Add in some null data to the new df to the columns 'longitude' and 'latitude' in randomly selected rows but make sure both columns don't have a missing value in the same row
# 6. Output the rows that contain missing values
# 7. Fill in the missing values by using the 'center_point_geom' column
# 8. Output the fully updated and fixed df that now doesn't have any missing values (verify that there aren't any missing values left)
# 9. Create and plot a bar chart (use sns and annotate each bar in the plot) of: yearly strike totals per quarter in 2020-2024

#pip install matplotlib
#pip install pandas
#pip install seaborn
#pip install datetime
#pip install plotly
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime
import plotly.express as px

# Creates a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring, along with other columns
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

# Set some random entries to NaN in a random subset of rows in 'df_joined' for either longitude or latitude columns, but not both
num_null_rows = np.random.randint(1, len(df_joined) + 1) # random number of rows to set NaN values to (1-number of rows); determines how many rows to select

rows_to_nullify = np.random.choice(df_joined.index, num_null_rows, replace=False) # randomly selects which rows to introduce NaN values to, based on the subset of row indices that was determined by 'num_null_rows' ; determines which rows to select

# Set NaN values in selected rows for either longitude or latitude columns
for idx in rows_to_nullify: # iterate over each selected row index
    col_to_nullify = np.random.choice(['longitude', 'latitude']) # for each selected row, randomly choose to nullify either 'longitude' or 'latitude' (only one per row) 
    df_joined.loc[idx, col_to_nullify] = np.nan # gets the row and column location and sets that entry to NaN

df_joined
         date   center_point_geom  longitude  latitude  lightning_strikes zip_code           city                 state state_code # output
0  2020-09-14   POINT(-46.4 48.4)      -46.4      48.4                751    45392      San Diego            California         CA
1  2020-12-21   POINT(124.6 54.4)      124.6      54.4                714    62679     Washington  District of Columbia         DC
2  2022-05-08  POINT(-90.9 -51.2)      -90.9     -51.2                172    94726      Nashville             Tennessee         TN
3  2023-01-14  POINT(-174.8 -8.0)     -174.8       NaN                918    06698        Phoenix               Arizona         AZ
4  2024-09-21   POINT(-89.0 81.8)      -89.0       NaN                149    09015  Oklahoma City              Oklahoma         OK
..        ...                 ...        ...       ...                ...      ...            ...                   ...        ...
95 2024-09-18    POINT(10.5 -7.1)       10.5       NaN                406    55574        Memphis             Tennessee         TN
96 2023-02-08  POINT(167.8 -36.7)      167.8     -36.7                693    91055      Baltimore              Maryland         MD
97 2020-09-04   POINT(-88.4 56.4)        NaN      56.4                706    09433         Denver              Colorado         CO
98 2021-11-02  POINT(-68.9 -58.2)      -68.9     -58.2                747    56863     Louisville              Kentucky         KY
99 2024-10-17  POINT(-162.6 57.3)     -162.6      57.3                503    95142         Boston         Massachusetts         MA
print()

df_joined.info()

<class 'pandas.core.frame.DataFrame'> # output
RangeIndex: 100 entries, 0 to 99
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   date               100 non-null    datetime64[ns]
 1   center_point_geom  100 non-null    object
 2   longitude          88 non-null     float64
 3   latitude           87 non-null     float64
 4   lightning_strikes  100 non-null    int32
 5   zip_code           100 non-null    object
 6   city               100 non-null    object
 7   state              100 non-null    object
 8   state_code         100 non-null    object
dtypes: datetime64[ns](1), float64(2), int32(1), object(5)
memory usage: 6.8+ KB
None

rows_with_null = df_joined[df_joined.isnull().any(axis=1)] # contains only the rows (axis=1) where 'df_joined' has at least one NaN value
print("Here are the rows with missing values")
print()
rows_with_null

         date    center_point_geom  longitude  latitude  lightning_strikes zip_code          city                 state state_code # output
2  2024-05-15   POINT(108.6 -12.1)      108.6       NaN                381    95104   Albuquerque            New Mexico         NM
7  2022-02-10   POINT(127.2 -85.1)      127.2       NaN                743    17081       El Paso                 Texas         TX
22 2022-03-11     POINT(-1.4 89.6)        NaN      89.6                142    00169      Columbus                  Ohio         OH
27 2020-02-08   POINT(123.2 -43.3)        NaN     -43.3                667    10467   Los Angeles            California         CA
36 2021-09-19     POINT(48.1 53.7)       48.1       NaN                486    27512     Milwaukee             Wisconsin         WI
37 2021-10-20    POINT(33.0 -82.2)        NaN     -82.2                699    44947       El Paso                 Texas         TX
43 2021-09-21  POINT(-126.3 -40.4)        NaN     -40.4                518    47252     Las Vegas                Nevada         NV
52 2021-02-01    POINT(149.4 28.3)      149.4       NaN                460    13934       Phoenix               Arizona         AZ
54 2022-02-25    POINT(13.1 -79.8)       13.1       NaN                336    15595  Jacksonville               Florida         FL
76 2020-08-06   POINT(-50.8 -75.9)      -50.8       NaN                122    76380       Houston                 Texas         TX
89 2022-03-03    POINT(-10.0 22.3)      -10.0       NaN                272    04433        Dallas                 Texas         TX
97 2024-01-28    POINT(70.0 -29.3)        NaN     -29.3                506    55342    Washington  District of Columbia         DC

print()

# Define a function to extract longitude and latitude values
def extract_lon_lat(geom_string):
    lon_lat = geom_string.split('(')[1].split(')')[0].split()
    return float(lon_lat[0]), float(lon_lat[1])

# Extract longitude and latitude values from 'center_point_geom' column for rows with NaN values
extracted_values = rows_with_null['center_point_geom'].apply(lambda geom: pd.Series(extract_lon_lat(geom)))

# Assign the extracted values back to the original DataFrame using correct index alignment
df_joined.loc[rows_with_null.index, ['longitude', 'latitude']] = extracted_values.values

# Display the updated DataFrame info
print("Missing values should now be filled in after extracting them from 'center_point_geom'")
print("Let's verify that... ")
print()
print(df_joined.info())

<class 'pandas.core.frame.DataFrame'> # output
RangeIndex: 100 entries, 0 to 99
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   date               100 non-null    datetime64[ns]
 1   center_point_geom  100 non-null    object
 2   longitude          100 non-null    float64
 3   latitude           100 non-null    float64
 4   lightning_strikes  100 non-null    int32
 5   zip_code           100 non-null    object
 6   city               100 non-null    object
 7   state              100 non-null    object
 8   state_code         100 non-null    object
dtypes: datetime64[ns](1), float64(2), int32(1), object(5)
memory usage: 6.8+ KB
None

print()

# Check if there are any NaN values left in the df
if df_joined.isnull().values.any():
    print("There are missing values in the DataFrame and something went wrong!!!")
else:
    print("There are no missing values in the DataFrame, so here is what it now looks like:")
    print()
  
    df_final = df_joined
    df_final

         date   center_point_geom  longitude  latitude  lightning_strikes zip_code          city         state state_code # output
0  2023-02-09    POINT(29.1 38.2)       29.1      38.2                685    72672       Houston         Texas         TX
1  2024-05-17  POINT(-152.2 52.1)     -152.2      52.1                911    34043        Austin         Texas         TX
2  2021-01-25   POINT(125.1 19.4)      125.1      19.4                381    02582        Austin         Texas         TX
3  2024-05-19    POINT(85.4 31.8)       85.4      31.8                484    55318     Baltimore      Maryland         MD
4  2024-10-17   POINT(101.4 44.0)      101.4      44.0                451    88686     Nashville     Tennessee         TN
..        ...                 ...        ...       ...                ...      ...           ...           ...        ...
95 2020-10-19  POINT(152.1 -46.3)      152.1     -46.3                677    68037    Louisville      Kentucky         KY
96 2020-10-30  POINT(121.4 -90.0)      121.4     -90.0                119    86339       Phoenix       Arizona         AZ
97 2023-04-20  POINT(-70.3 -87.6)      -70.3     -87.6                604    48628     Nashville     Tennessee         TN
98 2023-07-26  POINT(106.2 -33.2)      106.2     -33.2                925    03531  Philadelphia  Pennsylvania         PA
99 2022-10-06    POINT(6.2 -29.9)        6.2     -29.9                482    81939   Los Angeles    California         CA

fig = px
