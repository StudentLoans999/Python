The Python string method isupper() returns True if a string consists of only uppercase characters.

Some examples:

print("XYZ".isupper())

is_it_upper = "Abc".isupper()
print(is_it_upper)
Sample output
True
False

Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

An example of expected behaviour:

my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)
Sample output
['def', 'lower', 'another lower', 'Capitalized']

def no_shouting(my_list: list): # function that returns the given string without all the strings that are composed of all uppercase characters
    new_list = [] # create an empty list

    for string in my_list: # loop through the entire given list
        if string.isupper() == False: # checks if element is not all upperchase characters
            new_list.append(string) # add element to new list

    return new_list # returns the given string with all the string that have all uppercase characters removed
    

# Testing the function
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)# ['def', 'lower', 'another lower', 'Capitalized']
