# Write your solution here
characters = "-"

while True: # keeps running until broken
    string = input("Please type in a string: ")
    print()
    print(string)
    index = len(string)
    print(f"{characters*index}")
    print()

    if string == "":
        break
