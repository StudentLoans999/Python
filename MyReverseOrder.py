Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h

# Write your solution here
input_string = input("Please type in a string: ")
index = 0

while index < len(input_string): # loops exactly the amount of characters in the string
    print(input_string[len(input_string) - index - 1]) # gets the character at the last position in the string (first run)
    index += 1 # for second run, the character is now the second to last position ... and so on
