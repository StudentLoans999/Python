Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3

Sample output
Please type in a number: 6
1
6
2
5
3
4

# Write your solution here
number = int(input("Please type in a number: "))
first_integer = 1 # initialize the first integer
second_integer = number # initialize the second integer to be 'number'

while first_integer <= second_integer or second_integer > first_integer: # loops until the first number is larger than 'number' or until the second number is less than the first number

    if first_integer <= number: # checks if first number is less than or equal to 'number' and outputs first number if so
        print(first_integer)

    if second_integer > first_integer: # checks if second number is greater than first number and outputs second number if so
        print(second_integer)

    first_integer += 1 # iterates through the loop to get closer to reaching 'number'
    second_integer -= 1 # iterates through the loop to get further from 'number'
