""" Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
 """
def isPalindrome(string):
    return string == string[::-1]






def longest_palindrome(input_string):
    #sanitize input:
    chars = {',','.',' '}
    delete_chars = dict.fromkeys(chars)
    input_string = input_string.lower().translate(input_string.maketrans(delete_chars))
    
    print("Input String:", input_string)

    longest_palindrome = ""
    for length in range(1, len(input_string)+1):
        for starting_point in range(0, len(input_string)):
            section  = input_string[starting_point:starting_point +length]
            section_is_palindrome = isPalindrome(section)
            if section_is_palindrome and len(section) > len(longest_palindrome):
                longest_palindrome = section
            print(starting_point, length, section, isPalindrome(section))




    chars = {',','.',' '}
    delete_chars = dict.fromkeys(chars)
    longest_palindrome = longest_palindrome.lower().translate(longest_palindrome.maketrans(delete_chars))
    
    return longest_palindrome


# def longest_palindrome(input_string):
#     # Longest palindrome algorithm with manacher's algorithm:
#     # add a '#' in between all chars of string:
#     input_string = '#' + input_string
#     for index in range(2, len(input_string)+2, 2):
#         input_string = input_string[:index] + '#' + input_string[index:]
#     input_string = input_string + '#'
#     print("Converted String: ", input_string)

#     radius = len(input_string) // 2
#     print("Radius: ", radius)



# def longest_palindrome(input_string):
#     max_length = 1000
#     return_string = ""
#     # if size of input_string is empty or 1, 
#     # return 0/1
#     if len(input_string) == 0 or len(input_string) == 1:
#         return input_string
#     # for #'s bigger than 1, we want to iterate
#     # through the entire word, and check our ranges
#     # for out of bounds:
#     for index in range(0, len(input_string)-1):
#         # revert left_index and right_index to default:
#         right_index = index + 1
#         sub_string = input_string[:right_index]
#         #if its a palindrome:
#         if isPalindrome(sub_string):
#             return_string = sub_string
#             #while loop to iterate through the string:
#             while right_index < len(input_string)-1:
#                 print("right_index: ", right_index)
#                 right_index += 1
#                 string = input_string[:right_index]
#                 # let forward 
#                 print("substring: ", sub_string)
#                 # if substring is a palindrome, then we expand substring:
#                 if isPalindrome(string):
#                     right_index += 1
#                     return_string = string
#                 else:
#                     break

#     return return_string


example1 = "i want to be a racecar driver"

print("Longest Palindrome String: ", longest_palindrome(example1))




