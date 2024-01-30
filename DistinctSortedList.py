Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]

def distinct_numbers(my_list: list): # function to sort and add distinct numbers from given list to a new list
    new_list = [] # create empty string

    for i in my_list: # loop through every value in the given list
        if i in new_list: # if value in given list has already been added to the new list then don't add it again
            continue

        new_list.append(i) # add new, distinct element to the new list

    sorted_list = sorted(new_list) # sort the new list


    return sorted_list # return the sorted new list

# Testing the function
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
