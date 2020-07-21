""" 
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal
 to the last integer of the previous row.
Example:
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element 
is present ) for this problem """

def binary_search_row(list, target):
  low = 0
  high = len(list) - 1
  while low <= high:
      mid = low + ((high - low) // 2)
      if list[mid] < target:
        low = mid + 1
      elif list[mid] > target:
        high = mid - 1
      else:
        return 1
  return 0


def matrix_search(matrix, target):
  row = 0
  #perform binary search on row[0] to get the list of where the elem can be:
  while row < len(matrix):
    print("Compare Last Item in Row: ", matrix[row][len(matrix[row])-1], "And Target: ", target)
    #check the last item in the row and the target:
    if matrix[row][len(matrix[row])-1] >= target:
        #Found the row it can potentially be in 
        list = matrix[row]
        return binary_search_row(list, target)
    #if it doesn't satisfy the condition, then iterate to the next row:
    row += 1
  # if it's out of bounds:
  return 0

# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 22

# print(matrix_search(matrix,target))