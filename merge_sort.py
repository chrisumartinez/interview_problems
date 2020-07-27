""" 
Given a list of unsorted numbers, sort them using the Merge Sort algorithm. 

Don't use the built-in sorted or list.sort() methods - the goal of this is to understand and implement the merge sort algorithm. """


""" 
if len(nums > 1)

# create two lists, one for the right half, one for the left half

bisect the list
left = merge_sort(left)
right = merge_sort(right)

#recursively call merge sort
these lists are now started


merge the sorted lists

return sorted_list
    else:
        return nums

 """
  
def merge_sort(nums):
    if len(nums) > 1:

        #cut it in half
        mid = len(nums) // 2
        left = nums[0:mid]
        right = nums[mid:]

        right = merge_sort(right)
        left = merge_sort(left)
        sorted_list = []

        #until at least one list is empty
        # check the head elem of each list
        #append smaller elem to sorted list



        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                #append the smaller one:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))

        #concatentate the rest of elements of the other list
        sorted_list.extend(right)
        sorted_list.extend(left)

    else:
        #were down to just 1:
        sorted_list = nums
    return sorted_list

# list = [1,5,2,5,19,2,6]
# print(merge_sort(list))