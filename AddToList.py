Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

An example of expected behaviour:

Sample output
How many items: 3
Item 1: 10
Item 2: 250
Item 3: 34
[10, 250, 34]
                                                                                                             
list = [] # create an empty list
items = int(input("How many items: ")) # int input from user
item_number = 1 # start the counting of items at 1, for labeling purposes below

while items > 0: # loop for 'items' times
    item_value = int(input(f"Item {item_number}: ")) # int input from user while the 'item_number' is output to let user know where in the list a new value is being created
    list.append(item_value) # adding 'item_value' to the end of the list
    item_number += 1 # iterates to the next item number to display
    items -= 1 # iterates to the next spot in the list to add an item to ; to end the loop after 'items' times

print(list) # output the updated list                                                                                                             
