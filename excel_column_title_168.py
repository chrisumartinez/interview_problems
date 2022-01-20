# Given an integer columnNumber, return its
# corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
# Example 4:

# Input: columnNumber = 2147483647
# Output: "FXSHRXW"

# 26^0 + 26^1 + 26^2 + 26^3...


def convertToTitle(columnNumber):
    offset = 65
    base = 26
    ans = ""

    while columnNumber:
        columnNumber, remainder = divmod(columnNumber - 1, base)
        ans += chr(remainder + offset)

    ans = ans[::-1]
    return ans


excelColumn = 52
# print(26 // 26)
print(convertToTitle(excelColumn))
