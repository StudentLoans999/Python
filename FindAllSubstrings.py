Please make an extended version of the previous program (FindFirstSubstring.py), which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word): # # loops through all the instances where the 'character' is found in 'word', and when there are at least two more letters following it in the word  
    if word[index] == character: # if in this position there is 'character'
        print(word[index:index+3]) # output a substring of the first instance of the 'character' to two more characters that follow it
    index += 1 # move to the next character in 'word' (iterates through the loop)
