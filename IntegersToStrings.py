Please write a function named formatted, which takes a list of floating point numbers as its argument. The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the list should remain unchanged.

Hint: use f-strings to format the floating point numbers into suitable strings.

An example of expected beahviour:

my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)
Sample output
['1.23', '0.33', '0.11', '3.45']

def formatted(my_list: list): # function that returns the integers in the list into floats rounded by two decimal places 
    new_list = [] # create an empty list

    for n in my_list: # loop through all the numbers in the given list
        new_list.append(f"{n:.2f}") # add all the elements to the new list, but as a float rounded to two decimal places

    return new_list # return the new list of all the rounded floats in the given list

# Testing the function
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    result = formatted(my_list)
    print(result) # ['1.23', '0.33', '0.11', '3.45']
