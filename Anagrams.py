Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False
Hint: the function sorted can be used on strings as well.

def anagrams(word1: str, word2: str) -> bool:
    # Sort the characters in both strings
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    return sorted_str1 == sorted_str2 # check if the sorted strings are equal

# Testing the function
print(anagrams("tame", "meta"))   # True
print(anagrams("tame", "mate"))   # True
print(anagrams("tame", "team"))   # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False
