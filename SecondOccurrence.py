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
 
index1 = string.find(substring) # look for the first instance of the 'substring' input, in 'string'
index2 = -1 # set this to see if the substring gets found or not

if index1 != -1: # if found the first occurrence of substring in string
    string = string[index1+len(substring):] # set the string to start at the first occurrence + the length of the substring (and goes to the end of the string)
    index2 = string.find(substring) # sets this to a new value to indicate that there is a second occurrence of substring in string ; sets it to look for substring in string
 
if index2 == -1: # there isn't a second occurrence of substring in string (since index2 was not changed from its initial value)
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".") # found second occurrence of substring in string after the first occurrence, and to make sure it doesn't overlap, get the length of substring
