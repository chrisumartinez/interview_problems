# Given a sorted array of distinct integers and a
# target value, return the index if the target is found.
# If not, return the index where it would be if it were
#  inserted in order.

# You must write an algorithm with O(log n)
# runtime complexity.


# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:

# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:

# Input: nums = [1], target = 0
# Output: 0

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    # BINARY SEARCH, THEN ADD IN BETWEEN:
    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:

        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # if not found, return low:
    return low


nums1 = [1, 3, 5, 6]
target1 = 5
nums2 = [1]
target2 = 2
target3 = 7
target4 = 0
target5 = 0
print(searchInsert(nums1, target1))  # Expect: 2
print(searchInsert(nums1, target2))  # Expect: 1
print(searchInsert(nums1, target3))  # Expect: 4
print(searchInsert(nums1, target4))  # Expect: 0
print(searchInsert(nums2, target5))  # Expect: 0
