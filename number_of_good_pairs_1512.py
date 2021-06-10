# 1512. Number of Good Pairs

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.


# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0


def numIdenticalPairs(nums):

    good_pairs = 0
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                good_pairs += 1

    return good_pairs


# nums = [1, 2, 3, 1, 1, 3]  # Expected: 4
# nums2 = [1, 1, 1, 1]
# nums3 = [1, 2, 3]
# print(numIdenticalPairs(nums))
# print(numIdenticalPairs(nums2))  # Expected: 6
# print(numIdenticalPairs(nums3))  # Expected: 0
