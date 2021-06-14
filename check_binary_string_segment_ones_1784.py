# Given a binary string s ​​​​​without leading zeros,
# return true​​​ if s contains at most one contiguous
# segment of ones. Otherwise, return false.

# Example 1:
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:
# Input: s = "110"
# Output: true
# Constraints:
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.


def checkOnesSegment(s):
    arr = [char for char in s]
    zero_flag = False

    for i in range(1, len(arr)):
        if arr[i] == "0":
            if not zero_flag:
                zero_flag = True
        else:
            # must be a one:
            # if zero flag has been tripped:
            if zero_flag:
                return False

    return True


s = "1001"
s2 = "110"
s3 = "100011"
s4 = "100000"
s5 = "10"
s6 = "1"

print(checkOnesSegment(s6))  # Expected: false
# print(checkOnesSegment(s2))  # Expected: true
# print(checkOnesSegment(s3))  # Expected False
# print(checkOnesSegment(s4))  # Expected: true
