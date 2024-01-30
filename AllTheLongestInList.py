Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.

The order of the strings in the returned list should be the same as in the original.

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']

def all_the_longest(my_list: list): # function that returns the length of the shortest string in the given list 
    longest_length = 0  # initialize (define the criteria wanted) the determining/comparison variable
    longest_list = [] # initialize an empty list

    for string in my_list: # loop through all the strings in the given list
        if len(string) >= longest_length: # check if the length of the current element is greater than or equal to the last greatest length (the longest previous string)

            if len(string) > longest_length: # check if the current element's length is greater than the longest length

                longest_length = len(string) # update the variable to be the length of the new element
                longest_list = [string]  # start a new list with the current element (or reset the new list to have only this one element)

            else:
                longest_list.append(string) # if the current element's length is equal to the longest length, append it to the new list

    return longest_list # return the list of all the longest strings in the given list

# Testing the function
if __name__ == "__main__":
    # First Example
    my_list = ["first", "second", "eleventh", "fourth"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    # Second Example
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
