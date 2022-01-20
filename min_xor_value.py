""" 
Given a list of unsigned integers, find the pair of 
integers in the array which have the minimum XOR value. 
Return the minimum XOR value.

 
Examples : 
Input 
0 2 5 7 
Output 
2 (0 XOR 2) 
Input 
0 4 7 9 
Output 
3 (4 XOR 7)
Constraints: 
2 <= N <= 100 000 
0 <= A[i] <= 1 000 000 000 """


#find the 2 numbers with most amount of 1's:

import math

def min_xor_value(nums):
    # find  2 smallest numbers:
    # sort num_list:
    nums = sorted(nums)
    min_value = 99999999

    for index in range(0, len(nums)-1):
        min_value = min(min_value, nums[index] ^ nums[index+1])
    return min_value


num_list = [0,4,7,9]
num_list_two = [0,2,5,7]

print(min_xor_value(num_list)) #Expected: 2
#print(min_xor_value(num_list_two)) #Expected: 3