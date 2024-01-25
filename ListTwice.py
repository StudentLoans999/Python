Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0.

An example of expected behaviour:

Sample output
New item: 3
The list now: [3]
The list in order: [3]
New item: 1
The list now: [3, 1]
The list in order: [1, 3]
New item: 9
The list now: [3, 1, 9]
The list in order: [1, 3, 9]
New item: 5
The list now: [3, 1, 9, 5]
The list in order: [1, 3, 5, 9]
New item: 0
Bye!

original_list = [] # create an empty list
sorted_list = original_list # counts up if adding a new word to the list

while True: # loops until break
    new_item = int(input("New item: ")) # intinput for user to enter a number

    if new_item == 0: # user input a '0'
        break # exit loop
    
    original_list.append(new_item) # add 'new_item' to the end of 'original_list'

    sorted_list = sorted(original_list) # sort 'original_list'

    print(f"The list now: {original_list}") # ouput the original order of the list
    print(f"The list in order: {sorted_list}") # output the sorted order of the list

print("Bye!") # output goodbye message
