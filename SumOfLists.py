Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.

An example of the function at work:

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]

def list_sum (list1: list, list2: list):
    if len(list1) == len(list2):

        new_list = [] # create empty string

        for i in range(len(list1)): # loop through every indices of the elements in given list ; EX: if list1 had 8 elements, then it would be range(8) and 'i' starts the current index at 0 and goes to the last element
            new_list.append(list1[i] + list2[i]) # sums the elements of each list at the same index and adds the solution to 'new_list'

        return new_list # return the new list

# Testing the function
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
