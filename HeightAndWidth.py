Please modify the previous program (Width.py) so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########

# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
characters = "#" # character to be outputted
characters *= width # determines how many 'characters' to output, which is 'width'

while height > 0: # loops 'height' times (so will make this many rows)
    print(f"{characters}")
    height -= 1
