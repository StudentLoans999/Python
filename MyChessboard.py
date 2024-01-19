Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

chessboard(3)
print()
chessboard(6)
Sample output
101
010
101

101010
010101
101010
010101
101010
010101
                                                                                                                                                                                                                        
# Write your solution here
def chessboard(size): # create the function and adds a parameter that is an integer that defines how big to make the chessboard
                                                                                                                                                                                                                        
    for a in range(size): # loops as many times as 'size' ; creates 'size' number of rows
        character = '1' if a % 2 == 0 else '0' # makes character equal 1 if the row is even (so starts off at row 0, so 'character' starts off being 1) and equal 0 if row is odd

        for b in range(size): # loops as many times as 'size' ; creates 'character' inside each 'size' number of rows
            print(character, end='') # outputs 'character' one after another (without adding a line in between)
            character = '1' if character == '0' else '0' # makes character equal 1 if it is '0' (so it started off as 1) and equal 0 if it was 1 ; flip flops 'character' between 1 and 0

        print() # then moves to the next line for the next row

# Testing the function
if __name__ == "__main__":
    chessboard(3)          
