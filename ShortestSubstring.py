Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test

# Write your solution here
user_input = input("Please type in a string: ")
string_length = len(user_input)
letter = user_input[0] # first letter
position = 0 # beginning position

while string_length > 0: # loops through the length of the string
    letter = user_input[:position + 1] # beginning of substring to the next letter
    print(letter)
    string_length -= 1 # to iterate through the loop
    position += 1 # to get the next letter of the string
