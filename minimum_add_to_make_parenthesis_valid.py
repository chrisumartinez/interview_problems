""" 
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Input
S.length <= 1000
S only consists of '(' and ')' characters.

Sample Output
input#1
())
output#1
1

input#2
(((
output#2
3

input#3
()
output#3
0


input#4
()))((
output#4
4 """


def minAddToMakeValid(S):
    #Set up a Stack to Push the parenthesis:
    stack = []
    #Iterate through the array:
    for character in S:
        #If its an opening parenthesis, then we push it into the stack:
        if character == '(':
            stack.append(character)
        else:
            #check if stack is empty:
            if not stack:
                #then we just append:
                stack.append(character)
            else:
                #theres characers in stacks:
                #if we find an opening parenthesis, then we pop it off the stack
                if stack[-1] == '(':
                    stack.pop()
                # if its a closing parenthesis, then we break the loop:
                else:
                    stack.append(character)

    return len(stack)
	
sampleInput = '())' # Expected: 1
input2 = '(((' # Expected: 3
input3 = '()' # Expected: 0
input4 = '()))((' # Expected: 4
input5 = '' # Expected: 0

print(minAddToMakeValid(sampleInput))
print(minAddToMakeValid(input2))
print(minAddToMakeValid(input3))
print(minAddToMakeValid(input4))
print(minAddToMakeValid(input5))
