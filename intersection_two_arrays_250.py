# Given two integer arrays nums1 and
# nums2, return an array of their intersection.
# Each element in the result must appear as
# many times as it shows in both arrays and
# you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:

    # make a hash table, insert all the items of nums1:
    numDict = {}
    result = []

    for num in nums1:
        if num not in numDict:
            numDict[num] = 1
        else:
            numDict[num] += 1
    # now compare the items of num2 into the hashTable
    for num in nums2:
        if num in numDict:
            if numDict[num] != 0:
                result.append(num)
                numDict[num] -= 1
    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))