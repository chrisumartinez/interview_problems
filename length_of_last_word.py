""" 
 Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Given s = "Hello World",
return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
"""

def length_of_last_word(words):
    # check for an empty string
    if len(words) == 0:
        return 0
    # reverse the string:
    words = words[::-1]
    index = 0
    last_word = ""
    # while loop that will stop at first white space char:
    while words[index] != " ":
        # concatenate the string with the character:
        last_word += words[index]
        index += 1
        if index >= len(words):
            break

    # return the len of string:
    return len(last_word)

string1 = "Hello World"
string2 = ""
string3 = "  nonsense"
string4 = "checking fo a list of strings"
string5 = "aaa"
print(length_of_last_word(string1))
print(length_of_last_word(string2))
print(length_of_last_word(string3))
print(length_of_last_word(string4))
print(length_of_last_word(string5))

