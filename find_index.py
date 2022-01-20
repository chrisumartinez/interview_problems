""" 
Given a sorted array and a target value, return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.
You may assume no duplicates in the array.

Examples:

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0 """

def find_index(sorted_list, target):
    #Due Binary Search Method:
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = low + int((high-low) / 2)

        if sorted_list[mid] > target:
            high = mid - 1
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            return mid
    return low

list = [1,3,5,6]
target1 = 5
target2 = 2
target3 = 7
target4 = 0
print(find_index(list, target1))
print(find_index(list, target2))
print(find_index(list, target3))
print(find_index(list, target4))
