def column_correct(sudoku: list, column_no: int) -> bool: # Returns True or False depending on if each number from 1 to 9 appears at most once in the column specified in the Sudoku board
    col_values = [row[column_no] for row in sudoku] # initialize the column specified ; a list containing the elements from the specified column across all rows in the Sudoku board

    # Check if each number from 1 to 9 appears at most once in the column
    for i in range(1, 10): # iterates over the entire length of the column in the Sudoku board, but binding 'i' to 1-9
        if col_values.count(i) > 1: # if this number has been repeated in the column, then return False
            return False

    return True # return True if all the elements in the specified column are unique (excluding 0)

# Example Sudoku grid
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

# Testing the function
print(column_correct(sudoku, 0))  # False
print(column_correct(sudoku, 1))  # True
print(column_correct(sudoku, 2))  # True
