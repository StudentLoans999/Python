Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e, i, o, or u.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

# Write your solution here
user_input = input("Please type in a string: ")
if "a" in user_input:
    print("a found")
else:
    print("a not found")

if "e" in user_input:
    print("e found")
else:
    print("e not found")

if "i" in user_input:
    print("i found")
else:
    print("i not found")

if "o" in user_input:
    print("o found")
else:
    print("o not found")

if "u" in user_input:
    print("u found")
else:
    print("u not found")
