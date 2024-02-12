Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.

An example of how the function should work:

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))
Sample output
3

def count_matching_elements(my_matrix: list, element: int): # goes through each element in the 2D matrix and outputs the count of how many of them match the specified target element 
    number_of_element = 0 # initialize count of the element

    for i in range(len(my_matrix)): # iterate over each row in the matrix
        for j in range(len(my_matrix[i])): # iterate over each element in the current row

            if my_matrix[i][j] == element: # check if the current matrix element is equal to the target element
                number_of_element += 1 # increment the counter if a match is found

    return number_of_element # return the total count of matching elements

# Testing the function
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1)) # 3
