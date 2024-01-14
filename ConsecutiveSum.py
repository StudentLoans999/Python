Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

# Write your solution here

# Initialize variables
limit = int(input("Limit: "))
current_sum = 0
current_number = 1
calculation = ""

# Keep adding consecutive numbers until the sum is at least equal to the limit
while 0 < limit and current_sum < limit:
    current_sum += current_number
    calculation += str(current_number)
    current_number += 1
    
    # Add "+" if there are more numbers to be added; adds to the string the newest number
    if current_sum < limit:
        calculation += " + "

print(f"The consecutive sum: {calculation} = {current_sum}")
