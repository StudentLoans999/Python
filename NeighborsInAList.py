Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

An example function call:

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))
Sample output
4

def longest_series_of_neighbours(my_list: list) -> int: # function that returns the length of the longest list of neighbors (two consecutive items in the list are neighbours if their difference is 1)
    max_length = 1 # initialize max series of neighbors length variable (the fi rst element is part of the series)
    current_length = 1 # initialize current series length variable

    for i in range(1, len(my_list)): # loop through the given list starting from the second element
        if abs(my_list[i] - my_list[i - 1]) == 1: # check if the current and previous elements are neighbors (difference is 1)
            current_length += 1 # increment the current series length

        else: # the current and previous elements are not neighbors
            max_length = max(max_length, current_length) # update the maximum series length
            current_length = 1 # reset the current series length

    # Check the length of the last series
    max_length = max(max_length, current_length)

    return max_length # returns the length of the longest list of neighbors
    

# Testing the function
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))# 4
