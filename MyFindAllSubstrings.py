Please make an extended version of the previous program (FindFirstSubstring.py), which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

# Write your solution here
word = input("Please type in a string: ")
character = input("Please type in a character: ")
index = word.find(character) # look for the first instance of the 'character' input, in 'word'

while index != -1 and len(word) - index >= 3: # loops through all the instances where the 'character' is found in 'word', and when there are at least two more letters following it in the word  
    print(word[index:index +3]) # output a substring of the first instance of the 'character' to two more characters that follow it
    index = word.find(character, index + 1) # moves on to the next place in 'word' where 'character' is found (iterates through the loop)
