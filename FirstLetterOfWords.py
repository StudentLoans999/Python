Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w

# Write your solution here
sentence = input("Please type in a sentence: ")
 
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence
 
# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence): # loops through the whole string 'sentence' 
    if sentence[index-1] == " " and sentence[index] != " ": # checks if the character before 'index' (1, so 0 the first character) is a space and if the character wehere 'index' (1) is, is not a space 
        print(sentence[index]) # output the character at 'index'
    index += 1 # to iterate through the whole 'sentence'
