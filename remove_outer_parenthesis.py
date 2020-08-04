""" 
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".


Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".


Example 3:
Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:
S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string """


def removeOuterParentheses(string):
    #Assuming that String is a valid parenthesis:
    output = ""
    current_level = 0
    for character in string:
        if character == "(":
            current_level += 1
        if current_level > 1:
            output += character
        if character == ")":
            current_level -= 1
    return output


test1 = "(()())(())" #Expected: "()()()"
test2 = "" #Expected: ""
test3 = "(()())(())(()(()))" #Expected: "()()()()(())"
test4 = "()()" #Expected: ""
test5 = "(()(()))" #Expected: ()(())

print("Test 1: ", removeOuterParentheses(test1))
print("Test 2: ", removeOuterParentheses(test2))
print("Test 3: ", removeOuterParentheses(test3))
print("Test 4: ", removeOuterParentheses(test4))
print("Test 5: ", removeOuterParentheses(test5))
