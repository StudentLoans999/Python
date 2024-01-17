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
first_integer = 2 # initialize the first number of the pair (make this one larger than the second integer in order to make it so that each pair of numbers is flipped) 
second_integer = 1 # initialize the second number of the pair

while first_integer <= number or second_integer <= number: # loop until either of the numbers of the pair are larger than 'number'
  
    if first_integer <= number: # checks if 'first_integer' (2) is less than or equal to 'number' and then output it if so
        print(first_integer)
      
    if second_integer <= number: # checks if 'second_integer' (2) is less than or equal to 'number' and then output it if so
        print(second_integer)

    first_integer += 2 # iterate through the "while" loop
    second_integer += 2 # iterate through the "while" loop
