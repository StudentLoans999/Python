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


# .iloc - integer-location based indexing for selection by position
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


# .loc - Access a group of rows and columns by label(s) or a boolean array
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
