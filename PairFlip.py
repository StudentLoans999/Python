Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

Sample output
Please type in a number: 5
2
1
4
3
5

Sample output
Please type in a number: 6
2
1
4
3
6
5

# Write your solution here
number = int(input("Please type in a number: "))
 
index = 1 # initialize the first number of the pair (make this one larger than the second integer in order to make it so that each pair of numbers is flipped) 

while index+1 <= number: # loop until the second number of the pair (index+1) is larger than 'number'
    print(index+1) # outputs the larger integer of the pair (make this one larger than the 'index' integer in order to make it so that each pair of numbers is flipped) 
    print(index) # outputs the smaller integer of the pair
  
    index += 2 # iterates though the "while" loop
 
if index <= number: # keep outputting the first number 'index' until it gets larger than 'number' (so if user input 5, then the last number printed will be 5)
    print(index)
