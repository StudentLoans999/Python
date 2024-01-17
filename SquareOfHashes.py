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
