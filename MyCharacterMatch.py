Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a

# Write your solution here
input_string = input("Please type in a string: ")

if len(input_string) > 1 and input_string[1] == input_string[len(input_string) - 2]: # if at least two characters, and second character matches second to last character
    character = input_string[1] # the second character
    print(f"The second and the second to last characters are {character}")
else:
    print(f"The second and the second to last characters are different")
