Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list))
print("The range of the list is", result)
Sample output
The range of the list is 4

def range_of_list(my_list: list):
    list_start = my_list[0] # get first value in list
    list_end= my_list[-1] # get last value in list
    list_range = list_end - list_start # get range of list (end value - start value)

    return list_range # return range of list

# Testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)
