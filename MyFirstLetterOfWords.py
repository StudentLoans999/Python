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

for word in sentence.split(): # loops through each word in the string 'sentence'
    print(word[0]) # outputs the beginning character in the string 'sentence'
