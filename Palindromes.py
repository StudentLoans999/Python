Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

Please also write a main function which asks the user to type in words until they type in a palindrome:

Sample output
Please type in a palindrome: python
that wasn't a palindrome
Please type in a palindrome: java
that wasn't a palindrome
Please type in a palindrome: oddoreven
that wasn't a palindrome
Please type in a palindrome: neveroddoreven
neveroddoreven is a palindrome!

NB:, the main function should not be within an if __name__ == "__main__": block

# String Slicing notation review: string[start:stop:step]
string = "Hello, World!"

# Get the entire string
print(string[:])          # Output: Hello, World!

# Get the first 5 characters
print(string[:5])         # Output: Hello

# Get characters from index 7 to the end
print(string[7:])         # Output: World!

# Get characters from index 3 to 8 (excluding 8)
print(string[3:8])        # Output: lo, W

# Get every second character (step of 2)
print(string[::2])        # Output: Hlo o!

# Reverse the string
print(string[::-1])       # Output: !dlroW ,olleH

# End of review

def is_palindrome(s: str) -> bool: # function to check if a string is a palindrome
    cleaned_str = "".join(char.lower() for char in s if char.isalnum()) # remove spaces and non-alphanumberic characters and converts to lowercase for case-insensitive comparison
    return cleaned_str == cleaned_str[::-1] # check if the cleaned string is equal to its reverse

def main():
    while True: # loops until broken
        user_input = input("Please type in a palindrome: ") # user input

        if is_palindrome(user_input): # checks if user input is a palindrome (returns True if so) by using the function created above
            print(f"{user_input} is a palindrome!") # output yes message
            break # end the while loop

        else: # user input is not a palindrome
            print("that wasn't a palindrome.") # output no message

if __name__ == "__main__": # run main function for testing
    main()
