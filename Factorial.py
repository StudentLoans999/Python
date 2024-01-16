Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

Some examples of expected behaviour:

Sample output
Please type in a number: 3
The factorial of the number 3 is 6
Please type in a number: 4
The factorial of the number 4 is 24
Please type in a number: -1
Thanks and bye!

Sample output
Please type in a number: 1
The factorial of the number 1 is 1
Please type in a number: 0
Thanks and bye!

# Write your solution here
while True: # loops infinitely until break
  
    number = int(input("Please type in a number: "))
  
    # Stop the "while" loop if 'number' is not a positive integer
    if number <= 0:
        break
 
    factorial = 1 # initialize 'factorial'
    new = 1 # initialize 'new'
  
    while new <= number: # loops until 'new' reaches 'number'
        factorial *= new # multiply current value of 'factorial' by 'new' (1) and make the product be the new 'factorial' value 
        new += 1 # iterates 'new' so that the 'factorial' value can increase 
 
    print(f"The factorial of the number {number} is {factorial}") # outputs the final 'factorial' value after the inner "while" loop finishes 
 
print("Thanks and bye!") # output message after outer "while" loop breaks
