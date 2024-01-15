Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

Sample output
Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

Sample output
Please type in a number: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

# Write your solution here

number = int(input("Please type in a number: "))
counter1 = 1
        
while counter1 <= number: # loop through all numbers starting at 'counter1' (1) and going to 'number'
    counter2 = 1
        
    while counter2 <= number: # loop through all numbers starting at 'counter2' (1) and going to 'number'
        
        print(f"{counter1} x {counter2} = {counter1*counter2}") # each loop multiply the 'counter1' number and the 'counter2' number together and output it
        counter2 += 1 # increase 'counter2' number so then 'counter1' can multiply to this new number in the next iteration
        
    counter1 += 1 # increase 'counter1' number so then 'counter2' can multiply to this new number in the next iteration
