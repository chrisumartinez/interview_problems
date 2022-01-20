# given an array of integers, find the subarrays that add up to a given number.

# example input: [1,7,4,3,1,2,1,5,1] desired sum: 7


def find_subrrays(arr, target):
    result = []
    left = 0
    right = 1
    total = 0
    while right <= len(arr):
        print("window: ", arr[left:right])
        if sum(arr[left:right]) == target:
            result.append(arr[left:right])
            right += 1
        if sum(arr[left:right]) < target:
            right += 1
        if sum(arr[left:right]) > target:
            left += 1

    return result


def kadaneAlgo(nums):
    max_int = -99999
    maximum = 0
    result = []

    for i in range(len(nums)):
        maximum = max(nums[i], (nums[i] + maximum))
        if maximum > max_int:
            max_int = maximum

    print("result: ", result)
    return max_int


arr = [1, 2, 7, -4, -7, 4, -1, 9, -9]
arr2 = [1, 1, 1]
arr3 = [1, 2, 3]
arr4 = [3, 4, 2, 1, 3, 3, 1, 5, 7]
arr5 = [1]
arr6 = [-1, -3, -5]
target3 = 0
target = 7
target2 = 2
print(kadaneAlgo(arr))
