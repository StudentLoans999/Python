# Write your solution here
characters = "-" # character to be outputted

while True: # keeps running until broken
    string = input("Please type in a string: ")
    print()
    print(string)
    index = len(string)
    print(f"{characters*index}") # determines how many 'characters' to output, which is 'index'
    print()

    if string == "": # exits the loop when user inputs an empty string (presses Enter)
        break
