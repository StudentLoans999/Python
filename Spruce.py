Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

Calling spruce(3) should print out

Sample output
a spruce!
  *
 ***
*****
  *
Calling spruce(5) should print out

Sample output
a spruce!
    *
   ***
  *****
 *******
*********
    *
                                                                                                                                                  
def line(length : int, string : str): # function to print a line with repeated characters ( : int and : str are type hints)
    if len(string) > 0:
        print(f"{length * string[0]}") # if the string is not empty, print the first character in 'string' 'length' times
    else:
        string = "*" # if the string is empty, set it to "*" and print "*" 'length' times
        print(f"{length * string}")


# Write your solution here
def spruce(height) -> str: # (str is the return value of the function)
    rows = height
    width = 1
    original_spaces = height - width // 2 # store the initial number of leading spaces before the star in the first line of the spruce tree

    print("a spruce!")

    while rows > 0: # to loop through the number input to create that many rows of the spruce tree

        spaces = height - width // 2 # calculates the number of leading spaces to be printed before the stars in a particular line of the spruce tree (ensures that the leading spaces decrease as the width of the line increases) ; creates a pyramid-like shape for the spruce tree
        
        stars = width # to increase the number of stars to print this time in the loop 

        print(" " * spaces, end="") # print leading spaces but doesn't move on to the next line

        
        line(stars, "*") # print as many stars as 'stars' which increases by two every time it loops (and then the next line starts)

        width += 2 # increase the number of stars to print each loop
        rows -= 1 # to loop through the total height of input to create that many rows of the spruce tree

    print(" " * original_spaces, end="") # get the same number of spaces as the first line that was just a "*"
    line(1, "*") # print out just one "*" in the same line to end the spruce tree

# Testing the function
if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)
