""" Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.


Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned."""


#param: a -> String
def atoi(a):
    # Function first discards all whitespaces chars
    # Until the first non-white character is found.
    char = ' '
    num_set = {"0","1","2","3","4","5","6","7","8","9"}
    index = 0
    final_string = ''
    INT_MAX = (2 ** 32) - 1
    INT_MIN =  0 - (2 ** 31)

    #check for empty string:
    if (a == ""):
        return 0

    while char == a[index]:
        # We check if we are exceeding bounhds,
        # if we are, then return 0:
        if (index >= len(a)-1):
            return 0
        # while white_space chars, lets ignore, but increase index
        index += 1
        
    # Once we get the index of the first char, then we want to check
    # for a minus sign:
    if a[index] == '-':
        # we know it a negative number:
        # Iterate through rest of the string, bypass the '-'
        for char in range(index + 1, len(a)):
            # if the char == an actual #
            if a[char] in num_set:
                final_string += a[char]

        if (0 - int(final_string)) < INT_MIN:
            return INT_MIN
        else:
            return (0 - int(final_string))

    else:
        # Check if next char is not #, then return
        # Invalid: 0:
        if a[index] not in num_set:
            return 0

        #Positive
        # iterate through the string:
        for char in range(index, len(a)):
            if a[char] in num_set:
                final_string += a[char]
        if int(final_string) > INT_MAX:
            return INT_MAX
        else:
            return int(final_string)


# String1 = "42"
# String2 = "   -42"
# String3 = "4193"
# String4 = "words and 987"
# String5 = "-91283472332"
# String6 = "     "
# String7 = ""
# print(atoi(String1))
# print(atoi(String2))
# print(atoi(String3))
# print(atoi(String4))
# print(atoi(String5))
# print(atoi(String6))
# print(atoi(String7))