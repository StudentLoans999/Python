Please write a function named length which takes a list as its argument and returns the length of the list.

my_list = [1, 2, 3, 4, 5]
result = length(my_list))
print("The length is", result)

# the list given as an argument doesn't need to be stored in any variable
result = length([1, 1, 1, 1])
print("The length is", result)
Sample output
The length is 5
The length is 4

def length(my_list: list): # create a function with a list as the argument: length
    return len(my_list) # get the length of the list

# Testing the function
if __name__ == "__main__":
    # Example 1
    my_list = [1, 2, 3, 4, 5]
    result = length(my_list)
    print("The length is", result)

    # Example 2
    result = length([1, 1, 1, 1])
    print("The length is", result)
