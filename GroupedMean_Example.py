## Task: Group the means of each species (encoded as bytes) from data provided through a link

import numpy as np
import pandas as pd

# Get data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_data = pd.read_csv(url, names=('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')) # make a df from the link, with the specified columns

iris_data.head() # see what the data looks like

# Calculates the mean 'sepalwidth' for each 'species' in the dataset and returns a list containing the species name (encoded as bytes) and its corresponding mean sepal width
def get_grouped_mean():
    grouped_mean_sepalwidth = iris_data.groupby(['species'])['sepalwidth'].mean() # results is a Series object where the index contains the species names and the values contain the mean sepal widths
  
    result = [] # initializes an empty list which will store the species name and its mean sepal width in the desired format
    for species, mean_width in grouped_mean_sepalwidth.items(): # iterates over each item (species name and mean sepal width) in the grouped_mean_sepalwidth Series object
        result.append([species.encode(), mean_width]) # appends a sublist to the result list, containing the species name encoded as bytes using the encode() method (prefixed with 'b') and its corresponding mean sepal width
      
    return result # returns the result list containing the species names (encoded as bytes) and their corresponding mean sepal widths

# Calls the get_grouped_mean() function to calculate the grouped mean sepal widths, and then iterates over the result list grouped_mean, printing each sublist
grouped_mean = get_grouped_mean()
for i in grouped_mean:
    print(i)
  
## OUTPUT ##  
[b'Iris-setosa', 3.418]
[b'Iris-versicolor', 2.7700000000000005]
[b'Iris-virginica', 2.9739999999999998]
