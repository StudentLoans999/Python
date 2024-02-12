def print_grid(sudoku): # replaces zeroes in the sudoku board with _
  
    for row in sudoku: # iterates through every row
        for square in row: # iterates through every element in the row
          
            if square > 0:
                print(f" {square}", end="") # put the same number if it is not a zero
            else:
                print(" _", end="") # make '0' into a '_'
              
        print()

# Testing the function
if __name__ == "__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]
    print_grid(sudoku)

# Output
9 _ _ _ 8 _ 3 _ _
_ _ _ 2 5 _ 7 _ _
_ 2 _ 3 _ _ _ _ 4
_ 9 4 _ _ _ _ _ _
_ _ _ 7 3 _ 5 6 _
7 _ 5 _ 6 _ 4 _ _
_ _ 7 8 _ 3 9 _ _
_ _ 1 _ _ _ _ _ 3
3 _ _ _ _ _ _ _ 2
