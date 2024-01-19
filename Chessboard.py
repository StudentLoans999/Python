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
    i = 0 # initialize variable which is needed for "while" loop 

    while i < size: # loops as many times as 'size'
      
        if i % 2 == 0: # if even row number
            row = "10"*size # 'row' is created and it composed of a pattern of 10s one after another 'size' many times
        
        else: # if odd row number
            row = "01"*size # 'row' is created and it composed of a pattern of 01s one after another 'size' many times
          
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1 # iterate through "while" loop                                                                                                                                                                                                                        
                                                                                                                                                                                                                        
# Testing the function
if __name__ == "__main__":
    chessboard(3)          
