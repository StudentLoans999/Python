# zip() performs an element-wise combination of sequences

cities = ['Paris', 'Lagos', 'Mumbai']
countries = ['France', 'Nigeria', 'India']
places = zip(cities, countries)


print(places)
print(list(places))

# Output:
<zip object at 0x7f6b8f332908>
[('Paris', 'France'), ('Lagos', 'Nigeria'), ('Mumbai', 'India')]

# Unzipping

scientists = [('Nikola', 'Tesla'), ('Charles', 'Darwin'), ('Marie', 'Curie')]
given_names, surnames = zip(*scientists)
print(given_names)
print(surnames)

# Output:
('Nikola', 'Charles', 'Marie')
('Tesla', 'Darwin', 'Curie')
