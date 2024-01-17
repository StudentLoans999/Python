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

while first_integer <= second_integer or second_integer > first_integer: #

    if first_integer <= number:
        print(first_integer)

    if second_integer > first_integer:
        print(second_integer)

    first_integer += 1
    second_integer -= 1
