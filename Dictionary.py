# A 'dictionary' is a data structure that consists of a collection of key-value pairs 

## Different ways to create a dictionary
zoo = {'pen_1': 'penguins',
       'pen_2': 'zebras'
}
# or
zoo = dict(pen_1='penguins',
           pen_2='zebras',
)
# dict() allows you to do this:
zoo = dict(
          [
           ['pen_1', 'penguins'],
           ['pen_2', 'zebras'],
          ]
)

zoo['pen_2]'

# Output:
'zebras'

## Example of accessing a specific value in a dictionary
my_dict = {'nums': [1, 2, 3],
          'abc': ['a', 'b', 'c']
          }
print(my_dict['nums'])

# Output:
[1, 2, 3]

## Example of assigning a new value in a dictionary (continuing from above)
my_dict['floats'] = [1.0, 2.0, 3.0]
print(my_dict)

# Output:
{'nums': [1, 2, 3], 'abc': ['a', 'b', 'c'], 'floats': [1.0, 2.0, 3.0]}

## Example of deleting a value in a dictionary (continuing from above)
del my_dict['floats']
print(my_dict)

# Output:
{'nums': [1, 2, 3], 'abc': ['a', 'b', 'c']}

## Example of checking if a key exists in a dictionary (continuing from above)
print('floats' in my_dict)

# Output:
False

## Example of converting a list of tuples (representing the name, age, and position of a player on the team) into a dictionary

team = [
  ('Marta', 20, 'center'),
  ('Ana', 22, 'point guard'),
  ('Gabi', 22, 'shooting guard'),
  ('Luz', 21, 'power forward'),
  ('Lorena', 19, 'small forward'),
  ('Sandra', 19, 'center'),
  ('Mari', 18, 'point guard'),
  ('Esme', 18, 'shooting guard'),
  ('Lin', 18, 'power forward'),
  ('Sol', 19, 'small forward'),
]

# Efficient conversion
new_team = {} # initialize an empty dictionary named 'new_team'
for name, age, position in team: # iterate through each tuple in the 'team' list and for each tuple, extract the values for name, age, and position.
  
  if position in new_team: # check if the 'position' already exists as a key in 'new_team'
    new_team[position].append((name, age)) # append the tuple (name, age) to the existing list
  else:
    new_team[position] = [(name, age)] # create a new key with the 'position' and set its value as a list containing the tuple (name, age)
new_team # output the newly crated dictionary

# Output:
{
  'center': [('Marta', 20), ('Sandra', 19)],
  'point guard': [('Ana', 22), ('Mari', 18)],
  'shooting guard': [('Gabi', 22), ('Esme', 18)],
  'power forward': [('Luz', 21), ('Lin', 18)],
  'small forward': [('Lorena', 19), ('Sol', 19)]
}

# check if above works correctly
new_team['point guard']

# Output:
[('Ana', 22), ('Mari', 18)]

## Looping in a dictionary
for x in new_team:
  print(x)
  
# Output:
center
point guard
shooting guard
power forward
small forward

## Keys retrieval
new_team.keys()

# Output:
dict_keys(['center', 'point guard', 'shooting guard', 'power forward', 'small forward'])

## Values retrieval
new_team.values()

# Output:
dict_keys([[('Marta', 20), ('Sandra', 19)], [('Ana', 22), ('Mari', 18)], [('Gabi', 22), ('Esme', 18)], [('Luz', 21), ('Lin', 18)], [('Lorena', 19), ('Sol', 19)]])

## Keys and Values retrieval
for a, b in new_team.items():
  print(a, b)

# Output:
center [('Marta', 20), ('Sandra', 19)]
point guard [('Ana', 22), ('Mari', 18)]
shooting guard [('Gabi', 22), ('Esme', 18)]
power forward [('Luz', 21), ('Lin', 18)]
small forward [('Lorena', 19), ('Sol', 19)]
