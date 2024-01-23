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
  
Square of Hashes function:

Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

hash_square(3)
print()
hash_square(5)
Sample output
###
###
###

#####
#####
#####
#####
#####

def line(length, string): # first function

    if len(string) > 0: # checks if 'string' is not empty
        print(f"{length*string[0]}") # outputs the first character in 'string' 'length' many times

    else: # 'string' is empty
        string = "*" # adds a character which will be outputted
        print(f"{length*string}") # outputs the first character in 'string' 'length' many times


# Write your solution here
def hash_square(length): # define function and assign it the parameter of 'length'
    rows = length # initialize new variable by assigning it to the parameter 'length'
  
    while rows > 0: # loop until there are the number of rows input in the parameter 'length'
        character = '#' # initialize new variable that will be output and will create the square shape
        print(f"{character*length}") # output the 'character' 'length' times
        rows -= 1 # iterates so that there are 'length' number of rows outputted
      
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
    print()
    hash_square(5)
