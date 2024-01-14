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
