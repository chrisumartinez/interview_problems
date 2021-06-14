# Given a string s, return true if the s
# can be palindrome after deleting at most
# one character from it.


# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false


# def validPalindrome(s):
#     # check each time we cut a letter if its still a palindrome:
#     string = [char for char in s]
#     for i in range(len(string)):
#         temp = string.copy()
#         temp.pop(i)
#         if temp == temp[::-1]:
#             return True
#     return


def validPalindrome(s):
    left, right = 0, len(s) - 1
    # left and right boundaries:

    # while left is greater than right:

    while left < right:
        # if character of l does not match the character of r:
        if s[left] != s[right]:
            # even spliced array, and odd spliced array
            even, odd = s[left:right], s[left + 1 : right + 1]

            # return if either the remaining spliced array is a palindrome
            return even == even[::-1] or odd == odd[::-1]
        else:
            left += 1
            right -= 1

    # once all chars are checked, return True
    return True


s = "aba"
s2 = "abca"
s3 = "abc"
s4 = "racecar"
# print(validPalindrome(s))  # Expected: true
print(validPalindrome(s2))  # Expected: true
# print(validPalindrome(s3))  # Expected: false
# print(validPalindrome(s4))  # Expected: True
