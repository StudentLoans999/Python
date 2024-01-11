Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero. Print out how many numbers were typed in, the sum of them, the mean of them, how many were positive numbers and how many were negative numbers (The zero at the end should not be included in the calculations).

# Write your solution here
count = 0
sum = 0
positives = 0
negatives = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))

    if number == 0:
        break
    
    if number < 0:
        negatives += 1
    else:
        positives += 1

    count += 1
    sum += number

mean = sum / count
print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
