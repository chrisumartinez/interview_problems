""" Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Examples:
"Race Car" # returns 1

"Race a Car" # returns 0

"otto" # returns 1

"A man, a plan, a canal, Panama." # returns 1 """


def isPalindrome(str):
    chars = {',','.',' '}
    delete_chars = dict.fromkeys(chars)
    str = str.lower().translate(str.maketrans(delete_chars))
    left_bound = 0 ,
    right_bound = 0
    # Check if length is odd:
    if len(str) % 2 != 0:
        mid = len(str) // 2
        left_bound = mid - 1
        right_bound = mid + 1
        for index in range(mid, 0, -1):
            if str[left_bound] != str[right_bound]:
                return 0
            left_bound -= 1
            right_bound += 1
        return 1
    else:
        left_bound = (len(str) // 2) - 1
        right_bound = (len(str) // 2)
        mid = len(str) // 2
             
        for index in range(0,mid):
            if str[left_bound] != str[right_bound]:
                return 0
            left_bound -= 1
            right_bound += 1
        return 1
    
    


# string = "Race Car"
# string2 = "Race a Car"
# string3 = "otto"
# string4 = "A man, a plan, a canal, Panama."
# string5 = "abccba"

# print("Is the String a Palindrome?: " , string)
# print(isPalindrome(string))
# print("Is the String a Palindrome?: " , string2)
# print(isPalindrome(string2))
# print("Is the String a Palindrome?: " , string3)
# print(isPalindrome(string3))
# print("Is the String a Palindrome?: " , string4)
# print(isPalindrome(string4))
# print("Is the String a Palindrome?: " , string5)
# print(isPalindrome(string5))


