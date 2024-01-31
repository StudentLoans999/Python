Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

You can assume the string will contain only characters from the lowercase English alphabet a...z.

An example of expected behaviour:

my_string = "this is an example"
print(no_vowels(my_string))
Sample output
ths s n xmpl

def no_vowels(string: str) -> str: # function that returns the given string with all the vowels removed
    string_no_vowels = string # initialize the

    for char in string: # loop through the entire given string
        if char in 'aeiouyAEIOUY': # checks if element is a vowel
            string_no_vowels = string_no_vowels.replace(char, "") # removes the element (vowel) from the given string

    return string_no_vowels # returns the given string with all the vowels removed
    

# Testing the function
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))# ths s n xmpl
