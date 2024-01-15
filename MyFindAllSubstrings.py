Please make an extended version of the previous program (FindSubstrings.py), which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

# Write your solution here
word = input("Please type in a string: ")
character = input("Please type in a character: ")
index = word.find(character)

while index != -1 and len(word) - index >= 3:
    if len(word) == 0:
        break

    print(word[index:index +3])
    index = word.find(character, index + 1)
