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

Box of Hashes function:

Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.

Some examples of how the function should work:

box_of_hashes(5)
print()
box_of_hashes(2)
Sample output
##########
##########
##########
##########
##########

##########
##########

# Write your solution here
def line(length, string): # first function

    if len(string) > 0: # checks if 'string' is not empty
        print(f"{length*string[0]}") # outputs the first character in 'string' 'length' many times

    else: # 'string' is empty
        string = "*" # adds a character which will be outputted
        print(f"{length*string}") # outputs the first character in 'string' 'length' many times

def box_of_hashes(height): # second function

    while 0 < height: # loops 'height' many times ; creates 'height' many rows
        length = 10 # sets 'length' of the row
        string = "#" # sets the character that will be output in the row
        line(length, string) # runs the line function with the two variables above put in as the parameters
        height -= 1 # iterates over the loop

# Testing the function
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
