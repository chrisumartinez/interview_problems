from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    # get the values of rows and columns =>
    row = len(mat)
    col = len(mat[0])
    # check to see if reshape matrix is achieveable =>

    if row * col != r * c:
        return mat

    # get the all the items from the matrix:
    items = []
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            items.append(mat[i][j])

    # now that we have the items, create the resulting matrix =>
    counter = 0
    result = []
    for i in range(0, r):
        column = []
        for j in range(0, c):
            column.append(items[counter])
            counter += 1
        result.append(column)
    return result


mat = [[1, 2], [3, 4]]
r = 2
c = 4

print(matrixReshape(mat, r, c))  # [[1,2,3,4]]
