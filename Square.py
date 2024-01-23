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
  
Square function:

Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

square(5, "*")
print()
square(3, "o")
Sample output
*****
*****
*****
*****
*****

ooo
ooo
ooo
                                                                                                                                             
def line(length, string): # first function

    if len(string) > 0: # checks if 'string' is not empty
        print(f"{length*string[0]}") # outputs the first character in 'string' 'length' many times

    else: # 'string' is empty
        string = "*" # adds a character which will be outputted
        print(f"{length*string}") # outputs the first character in 'string' 'length' many times


# Write your solution here
def square(length, string): # define function and assign it the parameters of 'length' and 'string'
    rows = length # initialize new variable by assigning it to the parameter 'length'
  
    while rows > 0: # loop until there are the number of rows input in the parameter 'length'
        character = string # initialize new variable that will be output and will create the square shape
        print(f"{character*length}") # output the 'character' 'length' times
        rows -= 1 # iterates so that there are 'length' number of rows outputted
      
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")                                                                                                                                             
