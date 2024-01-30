Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)
Sample output
8
7

def length_of_longest(my_list: list): # function that returns the length of the longest string in the given list 
    longest = 0 # initialize (define the criteria wanted) the determining/comparison variable

    for string in my_list: # loop through all the strings in the given list
        if len(string) > longest: # check if the length of the current element is greater than the last greatest length (the longest previous string)
            longest = len(string) # assign the current element's length to be the new longest string 

    return longest # return the length of the longest string in the given list

# Testing the function
if __name__ == "__main__":
    # First Example
    my_list = ["first", "second", "eleventh", "fourth"]
    result = length_of_longest(my_list)
    print(result)

    # Second Example
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
