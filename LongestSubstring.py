Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test

# Write your solution here
user_input = input("Please type in a string: ")
string_length = len(user_input)
letter = user_input[len(user_input) - 1:]
position = len(user_input)

while string_length > 0:
    letter = user_input[position - 1:]
    print(letter)
    string_length -= 1
    position -= 1
