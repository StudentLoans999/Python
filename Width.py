Please write a program which prints out a line of hash characters, the width of which is chosen by the user.

Sample output
Width: 3

###
Sample output
Width: 8

########

# Write your solution here
width = int(input("Width: "))
characters = "#" # character to be outputted
characters *= width # determines how many 'characters' to output, which is 'width'
print(f"{characters}")
