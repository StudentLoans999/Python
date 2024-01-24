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
def spruce(height): # define function and assign it the parameter of 'height'
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
    spruce(3)
    print()
    spruce(5)      
