Please write a program which keeps asking the user for words. If the user types in end or if the user types in the same word twice (doesn't have to be consecutive), the loop ends and the program should print out the story the words formed.

# Write your solution here
story = ""
words_entered = set() # the set stores unique words input by the user

while True:
    code = input("Please type in a word: ")
    if code == "end" or code in words_entered: # user input "end" or a word they input previously, so end the loop
        break
    
    words_entered.add(code) # the user's input is added to the set
    story += code + " " # add the user's input to the story
print(story) # output all the user's inputs (story) when the loop ends
