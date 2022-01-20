""" 
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. 

This is consistent to C's strstr() and Java's indexOf(). """
def strStr(haystack, needle):
    needle_length = len(needle)
    # If Needle is an empty String, return empty
    if needle == "":
        return ""
    for index in range(len(haystack) - needle_length+1):
        # compare the needle to the substring
        if needle == haystack[index:index+needle_length]:
            return index
    return -1


# haystack = "aaaaa"
# needle = "bba"
# print("Index of first occurance: ", strStr(haystack, needle))