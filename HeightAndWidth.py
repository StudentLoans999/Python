# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
characters = "#" # character to be outputted
characters *= width # determines how many 'characters' to output, which is 'width'

while height > 0: # loops 'height' times (so will make this many rows)
    print(f"{characters}")
    height -= 1
