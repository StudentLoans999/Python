# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
characters = "#"
characters *= width # 

while height > 0:
    print(f"{characters}")
    height -= 1
