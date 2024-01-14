# Write your solution here
input_string = input("Please type in a string: ")

if len(input_string) > 1 and input_string[1] == input_string[len(input_string) - 2]: # if at least two characters, and second character matches second to last character
    character = input_string[1] # the second character
    print(f"The second and the second to last characters are {character}")
else:
    print(f"The second and the second to last characters are different")
