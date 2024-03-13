# enumerate() allows you to iterate over a sequence while keeping track of each element’s index

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters): # default starting index is 0
   print(index, letter)

# Output:
0 a
1 b
2 c

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, 2): # defined the starting index to 2
   print(index, letter)

# Output:
2 a
3 b
4 c
