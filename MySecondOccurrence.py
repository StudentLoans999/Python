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
first_occurrence = string.find(substring)

if first_occurrence != -1:
    second_occurrence = string.find(substring, first_occurrence + len(substring))
    
    if second_occurrence != -1:
        print(f"The second occurrence of the substring is at index {second_occurrence}.")

    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")

# Write your solution here
word = input("Please type in a string: ")
character = input("Please type in a character: ")
index = word.find(character) # look for the first instance of the 'character' input, in 'word'

while index != -1 and len(word) - index >= 3: # loops through all the instances where the 'character' is found in 'word', and when there are at least two more letters following it in the word  
    print(word[index:index +3]) # output a substring of the first instance of the 'character' to two more characters that follow it
    index = word.find(character, index + 1) # moves on to the next place in 'word' where 'character' is found (iterates through the loop)
