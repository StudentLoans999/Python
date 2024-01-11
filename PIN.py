![PIN](https://github.com/StudentLoans999/Python/assets/77641113/a7a3f39c-ac1c-48f0-b4b5-c51ee0580f62)

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
