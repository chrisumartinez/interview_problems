""" Given an NxN matrix, rotate it by 90 degrees. You should perform this operation in-place, using only constant memory.

Example:
starting matrix:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
once rotated by 90 degrees, the matrix becomes:
 [
  [7, 4, 1]
  [8, 5, 2]
  [9, 6, 3]
]

Hint:
Is there an easy way to rotate a coordinate pair by 90 degrees? """


def rotate_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            print(row,col)
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        matrix[row].reverse() # flip it backwards



# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# rotate_matrix(matrix)

""" 
0,0 -> 0,2
2,0 -> 0,0

0,1 -> 1,2
2,1 -> 0,1

0,2 -> 2,2
2,2 -> 0,2

1,0 -> 0,1
1,2 -> 2,1

1,1 -> 1,1 """




