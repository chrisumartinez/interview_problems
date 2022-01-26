def isPalindrome(x):
    stack = []
    while x != 0:
        digit = x % 10
        stack.append(digit)
        x = x // 10
    return stack == stack[::-1]


num = 121
print(isPalindrome(num))
