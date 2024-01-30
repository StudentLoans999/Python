Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

Sample output
***
*******
*
*
**

def list_of_stars(my_list: list):
    for value in my_list: # for loop that iterates every value in 'my_list' and prints out that many *s
        print(f"*"*value)

# Testing the function
if __name__ == "__main__":
    my_list = [3, 7, 1, 1, 2]
    result = list_of_stars(my_list)
