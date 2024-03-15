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
