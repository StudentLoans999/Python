Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)
Sample output
The result is 9

def sum_of_positives(my_list: list):
    list_positives = [] # create empty string

    for num in my_list: # loop through every value in given list
        if num > 0: # check if the iterated value is positive
            list_positives.append(num) # add positive value in given list to the new list

    list_sum = sum(list_positives) # sum up all the values in the new list

    return list_sum # return the new list

# Testing the function
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
