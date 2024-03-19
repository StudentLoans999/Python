## Task: Given a data file containing data about irises, find the grouped mean of a numeric column, sepal width, grouped by a categorical column, species, using NumPy
## The data will look like the following, where the first column is the sepal width and the fourth column is the species:
## 5.1,3.5,1.4,0.2,Iris-setosa ; 4.9,3.0,1.4,0.2,Iris-setosa ... 7.0,3.2,4.7,1.4,Iris-versicolor ; 6.4,3.2,4.5,1.5,Iris-versicolor ... 6.0,2.2,5.0,1.5,Iris-virginica ; 6.9,3.2,5.7,2.3,Iris-virginica
## The expected output should be in the following format: [b'Iris-setosa', 1.1111] ; [b'Iris-versicolor', 2.22222] ; [b'Iris-virginica', 3.3333]

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
