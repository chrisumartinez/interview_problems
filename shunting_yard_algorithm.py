""" 
Reverse polish notation is a postfix notation for mathematical expressions. For example, the infix expression
 (1 + 2) / 3 would become 1 2 + 3 /. More detailed explanation here: 
  https://en.wikipedia.org/wiki/Reverse_Polish_notation

Task:
Given a mathematical expression in reverse polish notation, represented by an array of strings,
find the answer to this expression. Operators consist only of +, -, *, /, and all numbers are integer values.
When performing a division on two numbers, use python's integer division operator (//). Your output should be a single integer,
which is the value of the expression when evaluated. Each expression is guaranteed to be valid.

Example 1:
expression = ["3", "4", "+", "5", "-"]
print(evaluate_expression(expression))
>> 2

Example 2:
expression = ["3", "4", "/", "5", "*"]
print(evaluate_expression(expression))
>> 0

Explanation 1:
"3 4 + 5 -" is equivalent to the infix expression "3 + 4 - 5"
The answer to this expression is 2.

Explanation 2:
"3 4 / 5 *" is equivalent to the infix expression "3 / 4 * 5"
Since we are using integer division, 3 / 4 = 0, and 0 * 5 = 0.
The answer to this expression is 0. """


def evaluate_expression(expression):
    stack = []
    for elem in expression:
        if elem == "+":
            #add 2 numbers, push total to stack
            total = 0
            total += int(stack.pop())
            total += int(stack.pop())
            stack.append(total)
        elif elem == "-":
            # subtract 2 popped #'s, push total to stack
            subtract = int(stack.pop())
            total = int(stack.pop()) - subtract
            stack.append(total)
        elif elem == "*":
            # Multiply 2 #'s, push total to stack
            total = int(stack.pop()) * int(stack.pop())
            stack.append(total)
        elif elem == "/":
            divisor = int(stack.pop())
            total = int(stack.pop()) // divisor
            stack.append(total)
        else:
            #its a number, just push to stack:
            stack.append(int(elem))

    return stack[0]
# expression = ["3", "4", "+", "5", "-"]
# expression2 = ["3", "4", "/", "5", "*"]
# print(evaluate_expression(expression))
# print(evaluate_expression(expression2))
# #Should Print 2

