# Write your solution here
input_string = input("Please type in a string: ")
index = -1

while index >= -len(input_string): # loops exactly the amount of characters in the string
    print(input_string[index]) # gets the character at the last position in the string (first run)
    index -= 1 # for second run, the character is now the second to last position ... and so on
