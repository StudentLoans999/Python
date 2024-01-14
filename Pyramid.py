n = 10 # number of layers in the pyramid
row = "*" # used to fill in the pyramid

while n > 0:
    print(" " * n + row) # goes 'n' spaces and outputs 'row' at that location 
    row += "**" # adds the next level to the pyramid
    n -= 1 # loops 'n' (10) times, so 10 rows in the pyramid
