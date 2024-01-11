Please write a program which keeps asking the user for words. If the user types in end or if the user types in the same word twice consecutively, the loop ends and the program should print out the story the words formed.

# Write your solution here
story = ""
last_word = None # initalizes last_word

while True:
    code = input("Please type in a word: ")
    if code == "end" or code == last_word: # user input "end" or a word they input last, so end the loop
        break
    
    last_word = code # updated the last word input
    story += code + " " # add the user's input to the story
print(story) # output all the user's inputs (story) when the loop ends
