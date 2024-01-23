Line function:

Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.

An example of expected behaviour:

line(7, "%")
line(10, "LOL")
line(3, "")
Sample output
%%%%%%%
LLLLLLLLLL
***
  
Triangle function:

Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

triangle(6)
print()
triangle(3)
Sample output
#
##
###
####
#####
######

#
##
###
                                                                                                                                                  
def line(length, string): # first function

    if len(string) > 0: # checks if 'string' is not empty
        print(f"{length*string[0]}") # outputs the first character in 'string' 'length' many times

    else: # 'string' is empty
        string = "*" # adds a character which will be outputted
        print(f"{length*string}") # outputs the first character in 'string' 'length' many times

# Write your solution here
def triangle(height): # define function and assign it the parameter of 'height'
    rows = height # initialize new variable by assigning it to the parameter 'height'
    width = 1                                                                                                                                                  
                                                                                                                                                  
    while rows > 0: # loop until there are the number of rows input in the parameter 'height'
      character = '#' # initialize new variable that will be output and will create the triangle shape

      while width <= height:
        
        print(f"{character*width}") # output the 'character' 'width' times
        width += 1
        
      rows -= 1 # iterates so that there are 'height' number of rows outputted
      
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)                                                                                                                                               
