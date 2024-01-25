Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.

The list is printed out in the beginning and after each operation. Have a look at the example execution below:

Sample output
The list is now []
a(d)d, (r)emove or e(x)it: d
The list is now [1]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: r
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: x
Bye!

list = [] # create an empty list
counter = 1 # counts up or down depending on if adding or removing to list

while True: # loops until break
    print(f"The list is now {list}") # output current status of list

    choice = input("a(d)d, (r)emove or e(x)it: ") # three choice input for user to either append or remove the newest number in the list or to exit out of the program

    if choice == 'd': # user input a 'd'
        list.append(counter) # add 'counter' to the end of 'list'
        counter += 1 # increase 'counter'

    elif choice == 'r' and len(list) != 0: # user input a 'r' and 'list' isn't empty (if it is empty, then loop runs again)
        list.pop(-1) # remove the number at the end of 'list'
        counter -= 1 # decrease 'counter'

    elif choice == 'x': # user input an 'x'
        break # exit loop

print("Bye!") # output goodbye message
