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
Add a ".", AACECAAAA.AAAACECAA Is this Palindrome? NO
Add 
 """

 
def minimumCharacters(word):
    counter = 0
    reverse_index =  1 - (len(word))
    print("word: ", word, "reversed: ", word[::-1]), 
    while word != word[::-1]:
        counter += 1
        word = word[reverse_index] + word
        reverse_index += 1
        print("word: ", word, "reversed: ", word[::-1]), 
        if counter == 5 or reverse_index >= 0:
            break
    return counter
        
string1 = "ABC"
string2 = "AACECAAAA"
print(minimumCharacters(string2))