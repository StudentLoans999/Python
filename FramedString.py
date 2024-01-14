Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

# Write your solution here
user_input = input("Word: ")
characters = "*"  # character to be outputted

print(f"{characters * 30}") # top of frame

middle = (29 - len(user_input)) // 2 # whitespace in frame (position to output string) ; used 29 since starting the frame with a 'characters'

spaces_count_even = middle
spaces_count_odd = middle - 1 # need to -1 for odd string length, otherwise length of the whole line would be 29, not 30
spaces = " " # whitespace to output

if len(user_input) % 2 == 0: # even length string
    frame = characters + (spaces * spaces_count_even) + user_input + (spaces * spaces_count_even) + characters # '*' + beginning whitespace + string + end whitespace + '*'   
  
else: # odd length string
    frame = (characters + (spaces * spaces_count_even) + user_input + (spaces * spaces_count_odd) + characters) # '*' + beginning whitespace + string + end whitespace (one space less than even) + '*'
  
print(frame)
print(f"{characters * 30}") # last line of frame
