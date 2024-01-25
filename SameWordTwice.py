Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

Sample output
Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words

list_of_words = [] # create an empty list
word_count = 0 # counts up if adding a new word to the list

while True: # loops until break
    new_word = input("Word: ") # input for user to enter a word to add to the list or to exit out of the program if they enter a word they entered in before

    if new_word in list_of_words: # user input a word they already input before
        break # exit loop

    else: # user input a brand new word
        list_of_words.append(new_word) # add 'new_word' to the end of 'list_of_words'
        word_count += 1 # increase 'word_count'

print(f"You typed in {word_count} different words") # output goodbye message, listing out the number of unique words input in the list
