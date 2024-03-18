# Series - a one-dimensional labeled array that can hold any data type. It’s similar to a column in a spreadsheet or a one-dimensional NumPy array. Each element in a series has an associated label called an index
# DataFrame - a two-dimensional labeled data structure—essentially a table or spreadsheet—where each column and row is represented by a Series

import pandas as pd

# Creating a DataFrame from a Dictionary then a Numpy Array, then a .csv

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df

   col1  col2 # output
0     1     3
1     2     4

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
df2

   a  b  c # output
0  1  2  3
1  4  5  6
2  7  8  9

df3 = pd.read_csv('/file_path/file_name.csv')

## Attributes
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df
df.columns # .columns - the column labels of the DataFrame

     A  B # output
0    1  3
1    2  4
Index(['A', 'B'], dtype='object')


# .dtypes - displays data type of each column
>>> df = pd.DataFrame({'float': [1.0],
...                    'int': [1],
...                    'datetime': [pd.Timestamp('20180310')],
...                    'string': ['foo']})
>>> df.dtypes

float              float64 # output
int                  int64
datetime    datetime64[ns]
string              object
dtype: object



### .iloc - integer-location based indexing for selection by position ###

>>> mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
...           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
...           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
>>> df = pd.DataFrame(mydict)
>>> df
      a     b     c     d # output
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

df.iloc[0] # indexing just the first row with a scalar integer
a    1 # output
b    2
c    3
d    4

df.iloc[[0]] # indexing just the first row with a list of integers
   a  b  c  d # output
0  1  2  3  4

df.iloc[[0, 1]] # indexing the first two rows with a list of integers
     a    b    c    d # output
0    1    2    3    4
1  100  200  300  400

df.iloc[:3] # indexing the first three rows with a slice object
      a     b     c     d # output
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

df.iloc[[True, False, True]] # indexing the first and third row with a boolean mask the same length as the index
      a     b     c     d # output
0     1     2     3     4
2  1000  2000  3000  4000


# Dataframe used for all the indexing done below #
      a     b     c     d 
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

df.iloc[0, 1] # indexing both axes using scalar integers; first row, second column
2 # output

df.iloc[[0, 2], [1, 3]] # indexing both axes using lists of integers; first row and third row then intersecting values at second column and fourth column ; displayed as first list done first
      b     d # output
0     2     4
2  2000  4000

df.iloc[1:3, 0:3] # indexing both axes using slice objects; second row and third row then first column through third column
      a     b     c # output
1   100   200   300
2  1000  2000  3000

df.iloc[:, [True, False, True, False]] # indexing both axes With a boolean array whose length matches the columns; ':' means the entire axis so all the rows, and then only the first and third columns
      a     c
0     1     3
1   100   300
2  1000  3000



### .loc - Access a group of rows and columns by label(s) or a boolean array ###

>>> df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
...                   index=['cobra', 'viper', 'sidewinder'],
...                   columns=['max_speed', 'shield'])
>>> df
            max_speed  shield # output
cobra               1       2
viper               4       5
sidewinder          7       8

df.loc['viper'] # getting a row as a Series by using a single label; the 'viper' row
max_speed    4 # output
shield       5

df.loc[['viper', 'sidewinder']] # getting two rows as a DataFrame by using a list of labels; the 'viper' and 'sidewinder' rows
            max_speed  shield # output
viper               4       5
sidewinder          7       8

df.loc['cobra', 'shield'] # getting a value by using a single label for row and column; the 'cobra' row intersecting with the 'shield' column
2 # output

df.loc['cobra':'viper', 'max_speed'] # getting values by using a slice with labels for the rows and a single label for the column; the 'cobra' and 'viper' rows with the 'max_speed' column
cobra    1 # output
viper    4

df.loc[[False, False, True]] # getting a row by using a Boolean list with the same length as the row axis; the third row only
            max_speed  shield # output
sidewinder          7       8

df.loc[pd.Series([False, True, False],
                 index=['viper', 'sidewinder', 'cobra'])] # getting a row by using an Alignable boolean Series; the second row only
                     max_speed  shield # output
sidewinder          7       8

df.loc[pd.Index(["cobra", "viper"], name="foo")] # getting rows by using Index; the 'cobra' and 'viper' rows with a name of 'foo'
       max_speed  shield # output
foo
cobra          1       2
viper          4       5

df.loc[df['shield'] > 6] # getting a boolean Series by using a Conditional; the rows with the values in the 'shield' column are greater than 6
            max_speed  shield # output
sidewinder          7       8

df.loc[df['shield'] > 6, ['max_speed']] # getting a boolean Series with column labels specified by using a Conditional; the rows with the values in the 'shield' column are greater than 6, but only values from the 'max_speed' column 
            max_speed # output
sidewinder          7

df.loc[(df['max_speed'] > 1) & (df['shield'] < 8)] # getting a boolean Series by using multiple Conditionals; the rows with the values in the 'max_speed' column are greater than 1 AND also where 'shield' is less than 8
            max_speed  shield # output
viper          4       5

df.loc[(df['max_speed'] > 4) | (df['shield'] < 5)] # getting a boolean Series by using multiple Conditionals; the rows with the values in the 'max_speed' column are greater than 4 OR where 'shield' is less than 8
            max_speed  shield # output
cobra               1       2
sidewinder          7       8


# Dataframe used for all the Setting values done below #
            max_speed  shield # output
cobra               1       2
viper               4       5
sidewinder    

df.loc[['viper', 'sidewinder'], ['shield']] = 50 # sets a value for the rows specified at the column specified; the 'viper' and 'sidewinder' rows in the 'shield' column values are set to 50
df
            max_speed  shield # output
cobra               1       2
viper               4      50
sidewinder          7      50

df.loc['cobra'] = 10 # sets a value for an entire row; 'cobra' row is set to 10
df
            max_speed  shield # output
cobra              10      10
viper               4      50
sidewinder          7      50

df.loc[df['shield'] > 35] = 0 # sets a value for rows matching the condition; the 'shield' column values that are greater than 35 will be set to 0 
df
            max_speed  shield # output
cobra              30      10
viper               0       0
sidewinder          0       0

df.loc["viper", "shield"] += 5 # sets a value at the specified location intersect; where the 'viper' row and the 'shield' column intersect will be set to 5 more than what it was
df
            max_speed  shield # output
cobra              30      10
viper               0       5
sidewinder          0       0

# 'viper' from the original dataframe is being added on top of 'cobra' in this new dataframe, 'cobra' to' viper' and 'sidewinder' to 'sidewinder'
shuffled_df = df.loc[["viper", "cobra", "sidewinder"]] # sets values by using a Series or a DataFrame, matching the index labels, not the index positions
df.loc[:] += shuffled_df
df
            max_speed  shield # output
cobra              60      20
viper               0      10
sidewinder          0       0


# Getting values on a DataFrame with an index that has integer labels #
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=[7, 8, 9], columns=['max_speed', 'shield'])
df
   max_speed  shield # output
7          1       2
8          4       5
9          7       8

df.loc[7:9] # slice with integer labels for rows (start and stop are included; gets the rows sepcified by the index's integer labels
   max_speed  shield # output
7          1       2
8          4       5
9          7       8


# Getting values using a DataFrame with a MultiIndex; 'cobra', 'sidewinder' and 'viper' are all an index row (label) with sub-rows (index tuple) in it called 'mark i' and 'mark ii' 
# Dataframe used for all the Getting values done below #
tuples = [
    ('cobra', 'mark i'), ('cobra', 'mark ii'),
    ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
    ('viper', 'mark ii'), ('viper', 'mark iii')
]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20],
          [1, 4], [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index) # 
df
                     max_speed  shield # output
cobra      mark i           12       2
           mark ii           0       4
sidewinder mark i           10      20
           mark ii           1       4
viper      mark ii           7       1
           mark iii         16      36

df.loc['cobra'] # gets all the values from the index (single label) specified (returns a DataFrame); 'cobra' index
         max_speed  shield # output
mark i          12       2
mark ii          0       4

df.loc[('cobra', 'mark ii')] # gets all the values from the index and sub-index (single index tuple) specified (returns a Series); 'cobra' index and 'mark ii' sub-index
max_speed    0 # output
shield       4
Name: (cobra, mark ii), dtype: int64

df.loc['cobra', 'mark i'] # gets all the values from the index and sub-index (single label for row and column) specified (returns a Series); 'cobra' index and 'mark i' sub-index
max_speed    12 # output
shield        2
Name: (cobra, mark i), dtype: int64

df.loc[[('cobra', 'mark ii')]] # gets all the values from the index and sub-index (single tuple) specified (returns a DataFrame); 'cobra' index and 'mark ii' sub-index
               max_speed  shield # output
cobra mark ii          0       4

df.loc[('cobra', 'mark i'), 'shield'] # gets the value from the index and sub-index (single tuple) with a column (single label) specified; where 'cobra' index and 'mark ii' sub-index intersect at the 'shield' column
2 # output

df.loc[('cobra', 'mark i'):'viper'] # gets all the values from the index and sub-index (single index tuple) specified to the single label specified (returns a DataFrame); 'cobra' index and 'mark i' sub-index sliced to 'viper' index rows
                     max_speed  shield # output
cobra      mark i           12       2
           mark ii           0       4
sidewinder mark i           10      20
           mark ii           1       4
viper      mark ii           7       1
           mark iii         16      36

df.loc[('cobra', 'mark i'):('viper', 'mark ii')] # gets all the values from the index and sub-index (single index tuple) specified to another single index tuple specified (returns a DataFrame); 'cobra' index and 'mark i' sub-index sliced to 'viper' index row, 'mark ii; subrow
                    max_speed  shield # output
cobra      mark i          12       2
           mark ii          0       4
sidewinder mark i          10      20
           mark ii          1       4
viper      mark ii          7       1



### .shape - Return a tuple representing the dimensionality of the DataFrame ###

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}) # returns number of rows and number of columns
df.shape
(2, 2) # output

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4], 
                   'col3': [5, 6]})
df.shape # returns number of rows and number of columns
(2, 3) # output



### .values - Return a Numpy representation of the DataFrame (axes labels will be removed) ###

df = pd.DataFrame({'age':    [ 3,  29],
                   'height': [94, 170],
                   'weight': [31, 115]})
df
print()
   age  height  weight # output
0    3      94      31
1   29     170     115

df.dtypes
age       int64
height    int64
weight    int64
dtype: object
print()

df.values
array([[  3,  94,  31],
       [ 29, 170, 115]])


df2 = pd.DataFrame([('parrot',   24.0, 'second'), # another example, but with mixed column types
                    ('lion',     80.5, 1),
                    ('monkey', np.nan, None)],
                  columns=('name', 'max_speed', 'rank'))
df2.dtypes
name          object # output
max_speed    float64
rank          object
dtype: object

df2.values
array([['parrot', 24.0, 'second'], # output
       ['lion', 80.5, 1],
       ['monkey', nan, None]], dtype=object)



### .apply - Apply a function along an axis of the DataFrame ###

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B']) # df to be used for examples below
df
   A  B # output
0  4  9
1  4  9
2  4  9

df.apply(np.sqrt) # applying a square root function to the df
     A    B # output
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0

df.apply(np.sum, axis=0) # applying a sum function on the y-axis
A    12 # output
B    27
dtype: int64

df.apply(np.sum, axis=1) # applying a sum function on the x-axis
0    13 # output
1    13
2    13
dtype: int64

df.apply(lambda x: [1, 2], axis=1) # returning a list-like will result in a Series
0    [1, 2] # output
1    [1, 2]
2    [1, 2]
dtype: object

df.apply(lambda x: [1, 2], axis=1, result_type='expand') # passing result_type='expand' will expand list-like results to columns of a Dataframe
   0  1 # output
0  1  2
1  1  2
2  1  2

df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1) # returning a Series inside the function is similar to passing result_type='expand'. The resulting column names will be the Series index
   foo  bar # output
0    1    2
1    1    2
2    1    2

# passing result_type='broadcast' will ensure the same shape result, whether list-like or scalar is returned by the function, and broadcast it along the axis. The resulting column names will be the originals
df.apply(lambda x: [1, 2], axis=1, result_type='broadcast')
   A  B # output
0  1  2
1  1  2
2  1  2



### .copy - Make a copy of this object’s indices and data ###

s = pd.Series([1, 2], index=["a", "b"]) # s to be used for example below
s
a    1 # output
b    2

s_copy = s.copy() # copies the entire series specified
s_copy
a    1 # output
b    2



### .describe - Generate descriptive statistics (options are: df.Series, df.datetime64, df.DataFrame, df.columnNameFromDataFrame ###

s = pd.Series([1, 2, 3]) # gets stats about the Series
s.describe()
count    3.0 # output
mean     2.0
std      1.0
min      1.0
25%      1.5
50%      2.0
75%      2.5
max      3.0



### .drop - Drop specified labels from rows or columns or can remove rows or columns by specifying label names and corresponding axis or by directly specifying index or column names ###
### (With a multi-index, different level labels can be removed by specifying the level ###

df = pd.DataFrame(np.arange(12).reshape(3, 4), # df to be used for examples below
                  columns=['A', 'B', 'C', 'D'])
df
   A  B   C   D # output
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

df.drop(['B', 'C'], axis=1) # drops columns 'B' and 'C', axis '1' is the columns (axis '0' is index labels); don't have to include 'axis' to get same output 
   A   D # output
0  0   3
1  4   7
2  8  11

df.drop([0, 1]) # drops a row by index '0' and '1'
   A  B   C   D # output
2  8  9  10  11


midx = pd.MultiIndex(levels=[['llama', 'cow', 'falcon'], # MultiIndex df to be used for examples below
                             ['speed', 'weight', 'length']],
                     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3, 0.2]])
df
                big     small # output
llama   speed   45.0    30.0
        weight  200.0   100.0
        length  1.5     1.0
cow     speed   30.0    20.0
        weight  250.0   150.0
        length  1.5     0.8
falcon  speed   320.0   250.0
        weight  1.0     0.8
        length  0.3     0.2

df.drop(index=('falcon', 'weight')) # drops the specified row; 'falcon' index's 'weight' row
                big     small # output
llama   speed   45.0    30.0
        weight  200.0   100.0
        length  1.5     1.0
cow     speed   30.0    20.0
        weight  250.0   150.0
        length  1.5     0.8
falcon  speed   320.0   250.0
        length  0.3     0.2

df.drop(index='cow', columns='small') # drops the index and the column specified; 'cow' index and 'small' column
                big # output
llama   speed   45.0
        weight  200.0
        length  1.5
falcon  speed   320.0
        weight  1.0
        length  0.3

df.drop(index='length', level=1) # drops the specified index level; 'length; index at level '1'
                big     small
llama   speed   45.0    30.0
        weight  200.0   100.0
cow     speed   30.0    20.0
        weight  250.0   150.0
falcon  speed   320.0   250.0
        weight  1.0     0.8



### .groupby - splits the object, applies a function, and combines the results (used to group large amounts of data) ###

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', # df used for example below
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df
   Animal  Max Speed # output
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0

df.groupby(['Animal']).mean() # groups the mean results by 'Animal'
        Max Speed # output
Animal
Falcon      375.0
Parrot       25.0


arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'], # MultiIndex df to be used for examples below
          ['Captive', 'Wild', 'Captive', 'Wild']]
index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]},
                  index=index)
df
                Max Speed # output
Animal Type
Falcon Captive      390.0
       Wild         350.0
Parrot Captive       30.0
       Wild          20.0

df.groupby(level=0).mean() # groups mean results by level '0' which is 'Animal'
        Max Speed # output
Animal
Falcon      370.0
Parrot       25.0

df.groupby(level="Type").mean() # groups mean results by level 'Type'
         Max Speed # output
Type
Captive      210.0
Wild         185.0



### .head - returns the first 'n' rows ###

df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion', # example df to be used for examples below
                   'monkey', 'parrot', 'shark', 'whale', 'zebra']})
df
      animal # output
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

df.head() # returns the first 5 rows (default), since no number was specified
      animal # output
0  alligator
1        bee
2     falcon
3       lion
4     monkey

df.head(3) # returns the first 3 rows
      animal # output
0  alligator
1        bee
2     falcon

df.head(-3) # returns all the rows except the last 3 rows
      animal # output
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot



### .info - prints a concise summary of a DataFrame ###

int_values = [1, 2, 3, 4, 5] # df to be used for example below
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
df = pd.DataFrame({"int_col": int_values, "text_col": text_values,
                  "float_col": float_values})
df
    int_col text_col  float_col # output
0        1    alpha       0.00
1        2     beta       0.25
2        3    gamma       0.50
3        4    delta       0.75
4        5  epsilon       1.00

df.info() # returns the full summary about the df
<class 'pandas.core.frame.DataFrame'> # output
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   int_col    5 non-null      int64
 1   text_col   5 non-null      object
 2   float_col  5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes

df.info(verbose=False) # returns summary without the per column info
<class 'pandas.core.frame.DataFrame'> # output
RangeIndex: 5 entries, 0 to 4
Columns: 3 entries, int_col to float_col
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes


df = pd.DataFrame({ # df for example below
    'Column_1': np.random.choice(['a', 'b', 'c'], 5),
    'Column_2': np.random.choice(['a', 'b', 'c'], 5),
    'Column_3': np.random.choice(['a', 'b', 'c'], 5)})
df
      Column_1 Column_2 Column_3 # output
0        c        c        b
1        b        a        a
2        b        c        b
3        c        a        a
4        a        a        a

df.info() # returns the full summary about the df
<class 'pandas.core.frame.DataFrame'> # output
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Column_1  5 non-null      object
 1   Column_2  5 non-null      object
 2   Column_3  5 non-null      object
dtypes: object(3)
memory usage: 248.0+ bytes
None



### .isna - returns a boolean same-sized object indicating if the values are NA; NA values (None or numpy.NaN) get mapped to True values and the rest are False (even empty strings or numpy.inf) ###

df = pd.DataFrame(dict(age=[5, 6, np.nan], # df to be used for example below
                       born=[pd.NaT, pd.Timestamp('1939-05-27'),
                             pd.Timestamp('1940-04-25')],
                       name=['Alfred', 'Batman', ''],
                       toy=[None, 'Batmobile', 'Joker']))
df
   age       born    name        toy # output
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

df.isna() # returns same-sized df with NA values marked as True
     age   born   name    toy # output
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False

ser = pd.Series([5, 6, np.nan]) # series to be used for example below
ser
0    5.0 # output
1    6.0
2    NaN
dtype: float64

ser.isna() # returns same-sized series with NA value marked as True
0    False # output
1    False
2     True
dtype: bool



### .sort_values - prints a concise summary of a DataFrame ###

df = pd.DataFrame({ # df to be used for examples below
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
df
  col1  col2  col3 col4 # output
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F

df.sort_values(by=['col1']) # sorts df by 'col1'
  col1  col2  col3 col4 # output
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

df.sort_values(by=['col1', 'col2']) # sorts df by 'col1' and 'col2'
  col1  col2  col3 col4 # output
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D

df.sort_values(by='col1', ascending=False) # sorts df by 'col1' descending
  col1  col2  col3 col4 # output
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D

df.sort_values(by='col1', ascending=False, na_position='first') # sorts df by 'col1' descending and 'NA's first
  col1  col2  col3 col4 # output
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B


df = pd.DataFrame({ # df for example below
    'Names': ['John', 'alice', 'Bob', 'Mary', 'ALICE', 'bob', 'JOHN']
})
df
   Names # output
0   John
1  alice
2    Bob
3   Mary
4  ALICE
5    bob
6   JOHN

sorted_df = df.sort_values(by='Names', key=lambda col: col.str.lower()) # sorts df by 'Names' and with the key function of lowercase first
   Names # output
1  alice
4  ALICE
2    Bob
5    bob
3   Mary
0   John
6   JOHN

sorted_df = df.sort_values(by='Names') # sorts df by 'Names' (the default sorting behavior is case sensitive, so capitals first)
   Names # output
2    Bob
5    bob
0   John
6   JOHN
3   Mary
1  alice
4  ALICE



### .value_counts - returns a Series containing the frequency of each distinct row in the DataFrame ###

df = pd.DataFrame({'num_legs': [2, 4, 4, 6], # df for examples below
                   'num_wings': [2, 0, 0, 0]},
                  index=['falcon', 'dog', 'cat', 'ant'])
df
        num_legs  num_wings # output
falcon         2          2
dog            4          0
cat            4          0
ant            6          0

df.value_counts() # returns a df listing out the distinct rows and adds a column at the end detailing how many in the original df there is of that row
num_legs  num_wings # output
4         0            2
2         2            1
6         0            1
Name: count, dtype: int64

df.value_counts(sort=False) # returns the value counts unsorted 
num_legs  num_wings # output
2         2            1
4         0            2
6         0            1

df.value_counts(ascending=True)  # returns the value counts sorted by ascending 
num_legs  num_wings # outp;ut
2         2            1
6         0            1
4         0            2

df.value_counts(normalize=True)  # returns the value counts normalized (proportions rather than frequencies) 
num_legs  num_wings # output
4         0            0.50
2         2            0.25
6         0            0.25
Name: proportion, dtype: float64


df = pd.DataFrame({'first_name': ['John', 'Anne', 'John', 'Beth'], # df used for examples below
                   'middle_name': ['Smith', pd.NA, pd.NA, 'Louise']})
df
  first_name middle_name # output
0       John       Smith
1       Anne        <NA>
2       John        <NA>
3       Beth      Louise

df.value_counts() # returns the value counts (without the 'NA' values)
first_name  middle_name # output
Beth        Louise         1
John        Smith          1

df.value_counts(dropna=False) # returns the value counts with the 'NA' values
first_name  middle_name #output
Anne        NaN            1
Beth        Louise         1
John        Smith          1
            NaN            1

df.value_counts("first_name") # returns the value counts of the 'first_name' column
first_name # output
John    2
Anne    1
Beth    1



### .mask - replaces values where the condition is True ###
### .where - replaces values where the condition is False ###

s = pd.Series(range(5)) # series to be used for examples below
s
0    0 # output
1    1
2    2
3    3
4    4

s.where(s > 0) # replaces values that are not greater than 0 to NaN
0    NaN # output
1    1.0
2    2.0
3    3.0
4    4.0

s.mask(s > 0) # replaces values that are greater than 0 to NaN
0    0.0 # output
1    NaN
2    NaN
3    NaN
4    NaN

s.where(s > 1, 10) # replaces values that are not greater than 1 with 10
0    10 # output
1    10
2    2
3    3
4    4

s.mask(s > 1, 10) # replaces values that are  greater than 1 with 10
0     0 # output
1     1
2    10
3    10
4    10


df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B']) # df used for example below; creates a df with 10 elements and 2 columns with automatic number of rows
# ('-1' rows means automatically calculate the number of rows based on the total number of elements '10' and and the specified number of columns '2')  
df
   A  B # output
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9

m = df % 3 == 0
df.where(m, -df) # replaces values that are not divisible by 3 with its negative version
   A  B # output
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9
