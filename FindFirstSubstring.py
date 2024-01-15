Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

Sample output
Please type in a word: mammoth
Please type in a character: m
mam

Sample output
Please type in a word: banana
Please type in a character: n
nan

Sample output
Please type in a word: tomato
Please type in a character: x

Sample output
Please type in a word: python
Please type in a character: n

# Write your solution here
word = input("Please type in a string: ")
character = input("Please type in a character: ")

index = word.find(character) # look for the first instance of the 'character' input, in 'word'
if index != -1 and len(word) - index >= 3: # if the character is found and if there are at least two more letters following it in the word
    print(word[index:index +3]) # output a substring of the first instance of the 'character' to two more characters that follow it
