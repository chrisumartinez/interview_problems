# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


def runningSum(nums):
    sums = [nums[0]]
    for i in range(1, len(nums)):
        sums.append(nums[i] + sums[-1])
    return sums


nums_one = [1, 2, 3, 4]  # expect [1,3,6,10]
nums_two = [1, 1, 1, 1, 1]  # expect [1,2,3,4,5]
nums_three = [3, 1, 2, 10, 1]  # expect [3,4,6,16,17]

print(runningSum(nums_one))
print(runningSum(nums_two))
print(runningSum(nums_three))
