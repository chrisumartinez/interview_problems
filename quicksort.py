def quickSort(nums):

    # handle the base case:
    if len(nums) == 0 or len(nums) == 1:
        return nums

    # grab the last value, set as the pivot:
    pivot = nums[-1]

    # make 2 arrays:x
    left = []
    right = []

    # divide the nums into left or right depending on value:
    for i in range(len(nums) - 1):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return quickSort(left) + [pivot] + quickSort(right)


nums = [10, 8, 2, 1, 6, 3, 9, 4, 7, 5]

print(quickSort(nums))
