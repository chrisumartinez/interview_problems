# Given the array nums, for each nums[i] find out
#  how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the
#  number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).


def smallerNumbersThanCurrent(nums):
    # n^2 algorithm:
    result = []
    for i in range(0, len(nums)):
        counter = 0
        for n in range(0, len(nums)):
            if i == 2:
                print("Counter: ", counter)
                print("nums[i]: ", nums[i], " nums[n]: ", nums[n])
            if nums[i] > nums[n]:
                counter += 1
        result.append(counter)
    counter = 0
    return result


nums = [6, 5, 4, 8]


print(smallerNumbersThanCurrent(nums))  # Expected: [1,0,3,1,4]
