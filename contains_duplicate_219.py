# Given an integer array nums and an integer k,
# return true if there are two distinct indices
#  i and j in the array such that nums[i] == nums[j]
#  and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    index_dict = {}
    for i in range(len(nums)):
        # print(index_dict)
        # print("i: ", i, " nums[i]: ", nums[i])

        if nums[i] not in index_dict:
            # add it:
            index_dict[nums[i]] = i
        else:
            # we find a duplicate, we compare the absolute value:
            if abs(index_dict[nums[i]] - i) <= k:
                # duplicate that satisfies the condition:
                return True
            else:
                # toss the preexisting value, update the value with the newest index:
                index_dict[nums[i]] = i
    return False


nums1 = [1, 2, 3, 1]
nums2 = [1, 0, 1, 1]
nums3 = [1, 2, 3, 1, 2, 3]
k = 3
k2 = 1
k3 = 2

print(containsNearbyDuplicate(nums1, k))
print(containsNearbyDuplicate(nums2, k2))
print(containsNearbyDuplicate(nums3, k3))
