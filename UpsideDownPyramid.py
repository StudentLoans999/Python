number = int(input("Please type in a number: ")) # number of rows to output
while number > 0:
    i = 0 # number that starts in the row
  
    while i < number: # loop one less times than the number inputted
        print(f"{i} ", end="") # output starting at 0 and going up to one less than the number inputted
        i += 1 # increase the number which will be output that will make up the row
      
    print() # output on to the next line after the inner loop is run
    number -= 1 # to loop through the number of rows to output
