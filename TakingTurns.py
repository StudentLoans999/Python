Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3

Sample output
Please type in a number: 6
1
6
2
5
3
4

# Write your solution here
number = int(input("Please type in a number: "))
 
left = 1 # initialize the left integer
right = number # initialize the right integer to be 'number'
 
while left < right: # loops until left integer is greater than right integer
  
    print(left) # outputs left integer
    print(right) # outputs right integer
  
    left += 1 # iterates through the loop to get closer to reaching 'number'
    right -= 1 # iterates through the loop to get further from 'number'

if left == right: # runs after "while" loop ; checks if left integer is equal to right integer and outputs left integer if so
    print(left)
