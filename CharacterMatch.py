word = input("Please type in a string: ")

if len(word) > 1 and word[1] == word[-2]: # if at least two characters, and second character matches second to last character
    print("The second and the second to last characters are " + word[1]) # the second character
else:
    print("The second and the second to last characters are different")
