Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.

# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
first_occurrence = string.find(substring) # look for the first instance of the 'substring' input, in 'string'

if first_occurrence != -1: # if found the first occurrence of substring in string
    second_occurrence = string.find(substring, first_occurrence + len(substring)) # look for the second instance of the 'substring' input, in 'string', after the first occurrence, and to make sure it doesn't overlap, get the length of substring
    
    if second_occurrence != -1: # if found the second occurrence of substring in string
        print(f"The second occurrence of the substring is at index {second_occurrence}.")

    else: # there isn't a second occurrence of substring in string
        print("The substring does not occur twice in the string.")
        
else: # there isn't a first occurrence of substring in string
    print("The substring does not occur twice in the string.")
