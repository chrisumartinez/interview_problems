# Given a string columnTitle that represents
# the column title as appear in an Excel sheet,
# return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
# Example 4:

# Input: columnTitle = "FXSHRXW"
# Output: 2147483647


def titleToNumber(columnTitle):
    base = 26
    offset = 65
    ans = 0
    exponent = 0
    columnTitle = columnTitle[::-1]
    for letter in columnTitle:
        value = (ord(letter) - offset) + 1
        ans += (base ** exponent) * value
        exponent += 1
    return ans


columnTitle = "ZY"
print(titleToNumber(columnTitle))
