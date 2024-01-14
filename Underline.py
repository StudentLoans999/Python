Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

Sample output
Please type in a string: Hi there!

Hi there!
---------
Please type in a string: This is a test

This is a test
--------------
Please type in a string: a

a
-
Please type in a string:

# Write your solution here
characters = "-" # character to be outputted

while True: # keeps running until broken
    string = input("Please type in a string: ")
    print()
    print(string)
    index = len(string)
    print(f"{characters*index}") # determines how many 'characters' to output, which is 'index'
    print()

    if string == "": # exits the loop when user inputs an empty string (presses Enter)
        break
