""" 
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Original Site:  https://www.interviewbit.com/problems/generate-all-parentheses/  """

def valid(parentheses):
  #Init Char Stack:
  char_stack = []
  for elem in parentheses:
    if elem == "(" or elem == "[" or elem == "{":
        char_stack.append(elem)
    elif elem == ")":
        if not char_stack:
            return 0
        if char_stack[-1] == "(":
            char_stack.pop()
        else:
            return 0
    elif elem == "]":
        if not char_stack:
            return 0
        if char_stack[-1] == "[":
            char_stack.pop()
        else:
            return 0
    elif elem == "}":
        if not char_stack:
            return 0
        if char_stack[-1] == "{":
            char_stack.pop()
        else:
            return 0
    if len(char_stack) != 0:
        return 0
    else:
        return 1
    
  """ 
  for the elem in parentheses:
      if the character is an opening bracket, then we push it into the stack.
      else if its a closing bracket, then we check with the top of the stack if its a matching open bracket
        if its not, then we return 0 immediately.
        if it is, then we pop the openning bracket.
   """

test1 = ["]", ")"] #Expected: 1: Valid
test2 = [")", "("] #Expected: 0: Invalid
test3 = ["(", "]"] #Expected: 0: Invalid
test4 = ["[", "("] #Expected: 0: Invalid

print(valid(test1))
print(valid(test2))
print(valid(test3))
print(valid(test4))