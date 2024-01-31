Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

An example of how the function should work:

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
Sample output
['erom eno', 'elpmaxe', 'ereht', 'iH']

# Adding to a List Review: .insert()

    #numbers = [1, 2, 3, 4, 5, 6]
    #numbers.insert(0, 10)
    #print(numbers)
    #numbers.insert(2, 20)
    #print(numbers)

    #Sample output
    #[10, 1, 2, 3, 4, 5, 6]
    #[10, 1, 20, 2, 3, 4, 5, 6]

# End of Review

def everything_reversed(my_list: list): # function that returns a new list with all of the items of the original list reversed and the order of items reversed as well
    new_list = [] # create an empty list
    string_reversed = "" # create an empty string


    for string in my_list: # loop through all the strings in the given list
        string_reversed = string[::-1] # set the string_reversed to be the reverse of the string element itself
        new_list.append(string_reversed) # add the reversed string into the end of the new list
    
    new_list = new_list[::-1] # reverse the order of elements in the new list

    return new_list # return the new list of all the elements reversed and in reverse order of the given list

# Testing the function
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    result = everything_reversed(my_list)
    print(result) # ['erom eno', 'elpmaxe', 'ereht', 'iH']
