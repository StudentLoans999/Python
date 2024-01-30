Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.

my_list = [1, 2, 3, 4, 5]
result = mean(my_list))
print("mean value is", result)
Sample output
mean value is 3.0

def mean(my_list: list):
    list_sum = sum(my_list) # sums all the integers in the list
    list_length = len(my_list) # gets the length of the list
    list_mean = list_sum / list_length # gets the mean of the list (sum / length)

    return list_mean # returns the mean value

# Testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)
