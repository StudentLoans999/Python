Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a

# Write your solution here

word = input("Please type in a string: ")

if len(word) > 1 and word[1] == word[-2]: # if at least two characters, and second character matches second to last character
    print("The second and the second to last characters are " + word[1]) # the second character
else:
    print("The second and the second to last characters are different")
