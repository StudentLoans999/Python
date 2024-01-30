Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.

An example of expected behaviour:

Sample output
Please type in a positive integer: 4
-4
-3
-2
-1
1
2
3
4

integer = int(input("Please type in a positive integer: ")) # int user input

for character in range(-integer, integer+1): # for loop with a range from negative of user input value to the user input value
    if character == 0: # when the value in the loop is 0 then just move on to the next number in the loop 
        continue
    print(character) # output the number in the loop
