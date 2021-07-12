# Given an integer array nums,
# return true if any value appears at
# least twice in the array, and return
# false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List


def containsDuplicate(nums: List[int]) -> bool:

    # use a set to contain the numbers that have been iterated throughout the list:
    num_set = set()
    for num in nums:
        if num not in num_set:
            num_set.add(num)
        else:
            return True
    return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
num2 = [1, 2, 3, 1]
print(containsDuplicate(num2))  # Expected true
