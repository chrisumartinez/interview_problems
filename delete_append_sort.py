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


#def da_sort(nums):
    # stack = []
    # num_operations = 0

    # #Iterate in n time
    # for index in range(0, len(nums)-1):
    #     #if first # isn't increasing with the next #, then push to stack, increment num_ops:
    #     if nums[index] > nums[index+1]:
    #         stack.append(nums[index])
    #         num_operations += 1

# input: an array of integers
# output: an integer, how many da operations are needed to sort this array
def da_sort(nums):
    #Just check for the longest subsequence of increasing integers, and count the
    stack = []
    counter = 0
    check = nums[0]
    for index in range(1, len(nums)):
        #check if the next number is bigger than the previous number:
        if check < nums[index]:
            # if it is, then lets increment our counter:
            counter += 1
            # The bigger # is now the one we want to use as a check:
            check = nums[index]
    # Once we iterate through our loop, then we compare the counter with the length of our array.
    # Because the length of the longest subsequence is 'counter', then we can subtract the length of counter
    # with the length of our entire array:
    
    #if its an already sorted array, then we don't have any delete append operations!
    if counter == 1:
        return 0
    else:
        return (len(nums) - counter)

array = [1, 3, 2]
array2 = [1, 5, 2, 4, 3, 6]
# array3 = [67890, 56312, 999999999, 12345, 23456, 38927, 45632, 100345, 98765, 23456,
# 87654, 43278, 23456, 117654, 321899, 25432, 54326, 217435, 26845, 31782,
# 33456, 41234, 56213]
#Subsequence = [1,5,6]
# length(array) - (len(subsequence) * 2)

#print(da_sort(array))
print(da_sort(array2))
#print(da_sort(array3))