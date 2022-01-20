""" 
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example:
Given [5, 7, 7, 8, 8, 10]
and target value 8,
return [3, 4].

Original Site:  https://www.interviewbit.com/problems/search-for-a-range/  """

#If the target is found, find range of the element
def create_range(array, found_index, target):
    left_bound = 0
    right_bound = 0
    return_range = []

    print("Found Index: ", found_index)

    #check left_bound
    for index in range(found_index-1, 0, -1):
        if array[index] == array[found_index]:
            left_bound = index
    #check right_bound
    for index in range(found_index, len(array)):
        if array[index] == array[found_index]:
            right_bound = index
    return_range.append(left_bound)
    return_range.append(right_bound)
    return return_range



def search_for_range(array, target):
    return_range = []
    #binary search for the location
    low  = 0
    high = len(array) - 1
    while low < high:
        mid = low + (high - low) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            #return the output of function
            return_range = create_range(array, mid, target)
            return return_range
    #if not found
    return [-1,-1]
            


array = [5,7,7,8,8,10]
target = 8
print(search_for_range(array, target))