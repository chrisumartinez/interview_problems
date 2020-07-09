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
    if string == string[::-1]:
        return True
    else:
        return False


def longest_palindrome(input_string):
    max = 1000
    return_string = ""
    # if size of input_string is empty or 1, 
    # return 0/1
    if len(input_string) == 0 or len(input_string) == 1:
        return input_string
    # for #'s bigger than 1, we want to iterate
    # through the entire word, and check our ranges
    # for out of bounds:
    for index in range(1, len(input_string)-1):
        # revert left_index and right_index to default:
        left_index = index - 1
        right_index = index + 1
        sub_string = input_string[:right_index]
        #if its a palindrome:
        if isPalindrome(sub_string):
            return_string = sub_string
            #while loop to iterate through the string:
            while left_index >= 0 and right_index <= len(input_string)-1:
                print("Index: ", index, "left_index: ", left_index, "right_index: ", right_index)
                left_index -= 1
                right_index += 1
                string = input_string[left_index:right_index]
                print("substring: ", sub_string)
                # if substring is a palindrome, then we expand substring:
                if isPalindrome(string):
                    left_index -= 1
                    right_index += 1
                    return_string = string
                else:
                    break

    return return_string


example1 = "babad"
example2 = "cbbd"
example3 = ""
example4 = "alskdnasldn asldjalkd"
print("Longest Palindrome String: ", longest_palindrome(example2))

