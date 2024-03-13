# A 'set' is a data structure that contains only unordered, non-interchangeable elements; each element must be immutable (hashable); a set is mutable
# So this will throw an error
example_0 = [1.5, {'a', 'b', 'c'}, 1.5]
set(example_0)

## Different ways to creat a set; to define an empty set, you have to use set()

x = set(['doo', 'car', 'caz', 'doo']) # a set containing a list
print(x)

{'car', 'doo', 'caz'} # output

x = set(('doo', 'car', 'caz', 'doo')) # a set containing a tuple
print(x)

{'car', 'doo', 'caz'} # output

x = set('doo') # a set containing a string
print(x)

{'o', 'd'} # output

# or

x = {'doo'}
print(type(x))

y = {}
print(type(y))

# Output
class 'set'
class 'dict'

x = {'doo'}
print(x)

{'doo'} # output

example_a = [1, 2, 2.0, '2']
set(example_a)

{1, 2, '2'} # output; 2 and 2.0 are evaluated as equivalent

example_b = ('apple', (1, 2, 2, 2, 3), 2)
set(example_b)

{2, 'apple', (1, 2, 2, 2, 3)} # output; a tuple is immutable (hashable) so is distinct

## Add to a set

example_c = {'mother', 'hamster', 'father'}
example_c.add('elderberries')
example_c

{'father', 'mother', 'elderberries', 'hamster'} # output

## intersection() - function that finds the elements that two sets have in common

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# Can use either one of the below to get the intersection
print(set1.intersection(set2)) 
print(set1 & set2)

{4, 5, 6} # output
{4, 5, 6} # same output for second print statement

## union() - function that finds all the elements from both sets

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

# Can use either one of the below to get the union
print(x1.union(x)) 
print(x1 | x2)

{'quux', 'bar', 'foo', 'qux', 'baz'} # output
{'quux', 'bar', 'foo', 'qux', 'baz'} # same output for second print statement

## difference() - function that finds the elements present in one set, but not the other

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# Can use either one of the below to get the difference
print(set1.difference(set2)) 
print(set1 - set2)

{1, 2, 3} # output
{1, 2, 3} # same output for second print statement

# Can use either one of the below to get the difference
print(set2.difference(set1)) 
print(set2 - set1)

{8, 9, 7} # output
{8, 9, 7} # same output for second print statement

## symmetric_difference() - function that finds elements from both sets that are mutually not present in the other

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# Can use either one of the below to get the symmetric_difference
print(set1.symmetric_difference(set2)) 
print(set2 ^ set1)

{1, 2, 3, 7, 8, 9} # output
{1, 2, 3, 7, 8, 9} # same output for second print statement


# A 'frozenset' is very similar to a 'set' except it is immutable

example_d = [1.5, frozenset(['a', 'b', 'c']), 1.5]
set(example_d)

{1.5, frozenset({'b', 'a', 'c'})} # output
