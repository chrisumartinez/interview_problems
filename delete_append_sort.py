""" 
You recently learned a new way to sort an array of numbers in your algorithms course. The algorithm sorts an array of numbers by repeatedly performing the Delete-and-Append operation. The Delete-and-Append operation consists of three steps:
Choose an element from the array.
Delete the chosen element from the array.
Append the chosen element to the end of the array.
Being a curious student, you wonder what is the minimum number of Delete-and-Append operations required to sort a given array.

Instructions:
Given an array of integers, find out the minimum number of Delete-Append operations that are required to make the array sorted. 

You can solve this problem in a number of ways. 
Hint 1: Could you somehow find out how many operations are necessary by looking at the already sorted version of the array?
Hint 2: Alternatively, it is possible to find out the minimum number of required operations without sorting the list?

Example:
[1, 5, 2, 4, 3, 6]; Starting array
[1, 5, 2, 3, 6, 4]; DA 4
[1, 2, 3, 6, 4, 5]; DA 5
[1, 2, 3, 4, 5, 6]; DA 6

Done! Took three operations.

Original site: https://open.kattis.com/problems/dasort  """



""" 
1. Initialize an empty stack
2. Iterate through the array
3. if the current elem > top of the stack and current elem  < smallest outcast:
3a. then we push into the stack
else:
    while current elem < top of the stack:
        pop off the top of the stack
        if top of the stack < smallest outcast:
            smallest outcast = smallest value in the stack
    push onto the stack

Array:
[1, 5, 2, 4, 3, 6]

smallest_outcast: 5

Stack:
[1,2,4]


len(array) - len(stack) = # of operations: 




 """


def da_sort(nums):
    in_order = []
    num_ops = None
    for num in nums:
        while len(in_order) > 0 and num < in_order[-1]:
            if num_ops == None or num < num_ops:
                num_ops = in_order.pop()
            else:
                in_order.pop()
        in_order.append(num)
    while in_order[-1] > num_ops:
        in_order.pop()
    return len(nums) - len(in_order)

list = [1, 5, 2, 4, 3, 6]
print(da_sort(list))


# def da_sort(nums):
#     stack = []
    
#     smallest_outcast = 2147483647
#     for elem in nums:
#         for item in stack:
#             if elem > slack[-1] and elem < smallest_outcast:
#                 #continue iterating, push onto stack
#                 stack.append(elem)
#             else:
#                 stack.pop()
#                 smallest_outcast = elem

#     return len(nums) -len(stack)

    

# array = [4,5,7,0,1,6,3]
# sorted_array = [0,1,3,4,5,6,7]

# array3 = [67890, 56312, 999999999, 12345, 23456, 38927, 45632, 100345, 98765, 23456,
# 87654, 43278, 23456, 117654, 321899, 25432, 54326, 217435, 26845, 31782,
# 33456, 41234, 56213]
#Subsequence = [1,5,6]

#print(da_sort(array))
#print(da_sort(array2))
#print(da_sort(array3))