# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:

    # binary search for our target #
    def binary_search(row, target):
        high = len(row) - 1
        low = 0

        while low <= high:
            mid = low + ((high - low) // 2)
            # 1print("mid: ", mid)
            if row[mid] == target:
                return True
            else:
                # check the rightside:
                if row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        # We never found the item in the matrix:
        return False

    # use a binary search to find if the number is either lower or higher than the number:
    list_number = -1
    for i in range(0, len(matrix)):
        if target == matrix[i][0]:
            # we found the target #:
            return True
        # we found the list to compare it to:
        if target < matrix[i][0]:
            list_number = i - 1
            break
    # if we went through the entire loop and the first number of each list was lower, then we check the last list to search:
    if list_number == -1:
        list_number = len(matrix) - 1

    # print("list_number: ", list_number)
    # print("List to check: ", matrix[list_number])

    # use binary search to locate the target =>
    return binary_search(matrix[list_number], target)


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
target2 = 13

print(searchMatrix(matrix, target))  # true
print(searchMatrix(matrix, target2))  # false
