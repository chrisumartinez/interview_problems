#
def mergeSort(nums):
    if len(nums) < 2:
        return nums
    return merge(
        mergeSort(nums[0 : len(nums) // 2]), mergeSort(nums[len(nums) // 2 : len(nums)])
    )


def merge(left, right):
    ans = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            ans.append(left[0])
            left.pop(0)
        else:
            ans.append(right[0])
            right.pop(0)
    # add remaining items from left and right into result:
    result = ans + left + right
    return result


nums = [10, 5, 3, 8, 2, 6, 4, 7, 9, 1]
print(mergeSort(nums))