Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)
Sample output
original [1, 2, 3, 4, 5]
new [2, 4]

def even_numbers(my_list: list):
    new_list = [] # create empty string

    for num in my_list: # loop through every value in given list
        if num % 2 == 0: # check if the iterated value is even
            new_list.append(num) # add even value in given list to the new list

    return new_list # return the new list

# Testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
