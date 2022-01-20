# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true

from typing import List


def isValid(s: str) -> bool:

    # use stacks to check legimitatcy of valid closing and opening parenthesis:
    stack = []
    for character in s:
        # check if the stack is empty, and if the next character is either an opening tag, or a tag that will close the topmost tag in the stack:
        if not stack:
            # if stack is empty, push onto the stack:
            stack.append(character)
        else:
            # check for closing tags:
            # make comparison to the necessary tag:
            if character == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif character == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif character == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                # its an opening tag:
                stack.append(character)
    if stack:
        return False
    else:
        return True


s = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"
print(isValid(s))  # true
print(isValid(s2))  # true
print(isValid(s3))  # false
print(isValid(s4))  # false
print(isValid(s5))  # true
