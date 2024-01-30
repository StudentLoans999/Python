Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)
Sample output
first
tim

def shortest(my_list: list): # function that returns the length of the shortest string in the given list 
    shortest_length = float('inf')  # initialize variable to positive infinity to ensure any length will be shorter
    shortest_string = "" # initalize string variable 

    for string in my_list: # loop through all the strings in the given list
        if len(string) < shortest_length: # check if the length of the current element is less than the last shortest length (the shortest previous string)

            shortest_length = len(string) # update the length of the shortest string comparison to be the new string's length (which is the new shortest length)
            shortest_string = string # assign the current element to be the new shortest string 

    return shortest_string # return the length of the shortest string in the given list

# Testing the function
if __name__ == "__main__":
    # First Example
    my_list = ["first", "second", "eleventh", "fourth"]
    result = shortest(my_list)
    print(result)

    # Second Example
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
