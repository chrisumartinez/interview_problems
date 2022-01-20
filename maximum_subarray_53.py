# Problem Link: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous
# subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

from typing import List


def maxSubArray(nums: List[int]) -> int:

    # Kadane's algorithm:
    max_int = -999999
    maximum = 0

    for i in range(0, len(nums)):

        maximum = max(nums[i], (nums[i] + maximum))

        if maximum > max_int:
            max_int = maximum

    return max_int


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [5, 4, -1, 7, 8]

print(maxSubArray(nums))  # Expected: 6
