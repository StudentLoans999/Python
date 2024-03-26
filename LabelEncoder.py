from sklearn.preprocessing import LabelEncoder

# Example 1 #

# Instantiate LabelEncoder() 
encoder = LabelEncoder()

data = [1, 2, 2, 6]

# Fit to the data
encoder.fit(data)

# Transform the data
transformed = encoder.transform(data)

# Reverse the transformation
inverse = encoder.inverse_transform(transformed)

print('Data =', data)
print('\n Classes: \n', encoder.classes_)
print('\n Encoded (normalized) classes: \n', transformed)
print('\n Reverse from encoded classes to original: \n', inverse)

# Output
Data = [1, 2, 2, 6]

 Classes: 
 [1 2 6]

 Encoded (normalized) classes: 
 [0 1 1 2]

 Reverse from encoded classes to original: 
 [1 2 2 6]


# Example 2 #

# Instantiate LabelEncoder()
encoder = LabelEncoder()

data = ['paris', 'paris', 'tokyo', 'amsterdam']

# Fit to the data
encoder.fit(data)

# Transform the data
transformed = encoder.transform(data)

# New data
new_data = [0, 2, 1, 1, 2]

# Get classes of new data
inverse = encoder.inverse_transform(new_data)

print('Data =', data)
print('\n Classes: \n', list(encoder.classes_))
print('\n Encoded classes: \n', transformed)
print('\n New data =', new_data)
print('\n Convert new_data to original classes: \n', list(inverse))

# Output
Data = ['paris', 'paris', 'tokyo', 'amsterdam']

 Classes: 
 ['amsterdam', 'paris', 'tokyo']

 Encoded classes: 
 [1 1 2 0]

 New data = [0, 2, 1, 1, 2]

 Convert new_data to original classes: 
 ['amsterdam', 'tokyo', 'paris', 'paris', 'tokyo']
