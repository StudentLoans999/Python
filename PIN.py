Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

Sample output
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts

If the user gets it right on the first try, the program should print out something a bit different:

Sample output
PIN: 4321
Correct! It only took you one single attempt!

# Write your solution here
attempts = 0 # initialize variable

while True: # this loop runs till the user inputs the correct PIN (4321)
    code = input("PIN: ")
    attempts += 1 # adds an attempt each time this loop is iterated

    if attempts == 1 and code == "4321": # User input the correct PIN on their first attempt
        first_attempt = True
        success = True
        break

    elif code == "4321": # user inputs the right PIN, so leaves the loop
        success = True
        break
    elif code != "4321": # reiterates over the loop since the user input the wrong PIN
        print("Wrong")

if success and first_attempt: # unique message to send to the user since they got the PIN right on their first attempt
    print("Correct! It only took you one single attempt!")

elif success: # generic message to send to the user since they got the PIN right after their first attempt
    print(f"Correct! It took you {attempts} attempts")
