Please write a program which keeps asking the user for words. If the user types in end or if the user types in the same word twice (doesn't have to be consecutive), the loop ends and the program should print out the story the words formed.

# Write your solution here
story = ""
words_entered = set()

while True:
    code = input("Please type in a word: ")
    if code == "end" or code in words_entered:
        break
    
    words_entered.add(code)
    story += code + " "
print(story)
