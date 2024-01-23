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
  
Shape function:

Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
Sample output
X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...
                                                                                                                                                  
def line(length, string): # first function

    if len(string) > 0: # checks if 'string' is not empty
        print(f"{length*string[0]}") # outputs the first character in 'string' 'length' many times

    else: # 'string' is empty
        string = "*" # adds a character which will be outputted
        print(f"{length*string}") # outputs the first character in 'string' 'length' many times


# Write your solution here
def shape(triangle_height, triangle_character, rectangle_height, rectangle_character): # define function and assign it the parameter of 'triangle_height'
    triangle_rows = triangle_height # initialize new variable by assigning it to the parameter 'triangle_height'
    triangle_width = 1                                                                                                                                                  
                                                                                                                                                  
    while triangle_rows > 0: # loop until there are the number of rows input in the parameter 'triangle_height'

      while triangle_width <= triangle_height:
        
        print(f"{triangle_character*triangle_width}") # output the 'triangle_character' 'triangle_width' times
        triangle_width += 1
        
      triangle_rows -= 1 # iterates so that there are 'triangle_height' number of rows outputted

    rectangle_rows = rectangle_height # initialize new variable by assigning it to the parameter 'rectangle_height'
                                                                                                                                                     
                                                                                                                                                  
    while rectangle_rows > 0: # loop until there are the number of rows input in the parameter 'rectangle_height'

      print(f"{rectangle_character*triangle_height}") # output the 'rectangle_character' 'triangle_height' times
        
      rectangle_rows -= 1 # iterates so that there are 'rectangle_height' number of rows outputted
      
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")                                                                                                                                   
