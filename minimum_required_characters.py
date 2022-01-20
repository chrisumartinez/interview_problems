""" 
Minimum Characters required to make a String Palindromic

You are given a string. The only operation allowed 
is to insert characters in the beginning of the string. 
Return the number of characters that are needed to be 
inserted to make the string a palindrome string

Examples:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2

ABC
add an A -> ABCA isPalindrome()? NO
add a B -> ABCAB isPalindrome()? NO
Add a ".", AACECAAAA.AAAACECAA Is this Palindrome? NO
Add 
 """


def isPalindrome(word):
    return word == word[::-1]


def minimumCharacters(word):
    if len(word) == 0 or len(word) == 1:
        return len(word)

    counter = 0
    # Append the reverse of each substring, starting from index 0 -> len(word)
    for index in range(0, len(word)):
        reversed_word = word[::-1]
        sub_string = reversed_word[:index]
        print("Sub_String: ", sub_string)
        if isPalindrome(sub_string + word):
            return counter
        else:
            counter += 1
    return counter


string0 = ""
string1 = "ABC"
string2 = "AACECAAAA"
print(minimumCharacters(string0))
print(minimumCharacters(string1))
print(minimumCharacters(string2))