Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

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

print(row_correct(sudoku, 0))
print(row_correct(sudoku, 1))
Sample output
True
False

def row_correct(sudoku: list, row_no: int) -> bool: # Returns True or False depending on if each number from 1 to 9 appears at most once in the specified row in the Sudoku board
    row_values = sudoku[row_no] # initialize the row specified

    # Check if each number from 1 to 9 appears at most once in the row
    for i in range(1, 10): # iterates over the entire length of the row in the Sudoku board, but binding 'i' to 1-9
        if row_values.count(i) > 1: # if this number has been repeated in the row, then return False
            return False

    return True # return True if all the elements in the specified row are unique (excluding 0)

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
print(row_correct(sudoku, 0))  # True
print(row_correct(sudoku, 1))  # False
print(row_correct(sudoku, 2))  # True
