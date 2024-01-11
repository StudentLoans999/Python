Please write a program which asks the user for a year, and prints out the next leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024

If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028

# Write your solution here
year = int(input("Year: "))
leap_year = year

# If the input year is a leap year, start looking for the leap year after that one
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    leap_year += 1

# Find the next leap year
while not (leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0)):
    leap_year += 1

print(f"The next leap year after {year} is {leap_year}")
