Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

An example of expected behaviour:


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
Sample output
howdydoody

def longest(my_list: list): # create a function that prints out the longest string in the given list
    longest_length = 0 # initialize (define the criteria wanted) the determining/comparison variable
    longest_string = "" # initialize the variable wanted, the longest string in the given list

    for string in my_list: # loop through all the strings in the given list
        if len(string) > longest_length: # check if the length of the current element is greater than the last greatest length (the longest previous string)
            longest_length = len(string) # assign the current element's length to be the new longest_length string (needed to compare to the next iteration) 
            longest_string = string # assign the current element's length to be the new longest string

    return longest_string # return the longest string in the given list

# Testing the function
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings)) # howdydoody
