Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

An example of expected behaviour:

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))
Sample output
b
e

def most_common_character(string: str) -> str: # function that returns the most commmon character within a given string (or the first one which appears if many characters with equal occurrences)
    max_count = 0 # initialize the number count of the most common character variable
    most_common_char = "" # initialize the most common character variable

    for char in string: # loop through the entire given string
        char_count = string.count(char) # count how many occurrences of the current element there are in the given string - set it to char_count
        
        # check if the current elements number of occurrences is greater than the last set max_count (highest number of occurrences previously)
        if char_count > max_count or (char_count == max_count and char < most_common_char): # also checks if the current character's count is equal to the maximum count seen so far. Finally, checks which character comes first in the string
            max_count = char_count # sets the max_count to the current elements count (since this new element occurs more than the last higheset count)
            most_common_char = char # sets the most_common_char to the current element (since this new element occurs more than the last higheset count)

    return most_common_char # returns the character that appeared the most in the given string (or the first one which appears if many characters with equal occurrences)
    

# Testing the function
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string)) # b | e
