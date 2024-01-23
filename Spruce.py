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
