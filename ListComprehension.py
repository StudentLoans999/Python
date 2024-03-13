"""
my_list = [expression for element in iterable if condition]

In this syntax:

expression refers to an operation or what you want to do with each element in the iterable sequence.

element is the variable name that you assign to represent each item in the iterable sequence.

iterable is the iterable sequence.

condition is any expression that evaluates to True or False. This element is optional and is used to filter elements of the iterable sequence.
"""

# This list comprehension adds 10 to each number in the list

numbers = [1, 2, 3, 4, 5]
new_list = [x + 10 for x in numbers] # 'x + 10' is the expression, 'x' is the element, and 'numbers' is the iterable sequence
print(new_list)

# Output:
[11, 12, 13, 14, 15]

# This list comprehension extracts the first and last letter of each word as a tuple, but only if the word is more than five letters long

words = ['Emotan', 'Amina', 'Ibeno', 'Sankwala']
new_list = [(word[0], word[-1]) for word in words if len(word) > 5] # 'word[0], word[-1]' is the expression, 'word' is the element, 'words' is the iterable sequence, and 'if len(word) > 5' is the condition
print(new_list)

# Output:
[('E', 'n'), ('S', 'a')]
