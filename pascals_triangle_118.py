# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


from typing import List


def generate(numRows: int) -> List[List[int]]:

    # base cases:

    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    result = [[1], [1, 1]]

    counter = 2
    while counter < numRows:
        # initalize our row:
        triangle_row = [1]
        # make a for loop to make the additions and append the sum to the row
        for i in range(0, len(result[counter - 1]) - 1):
            val = result[counter - 1][i] + result[counter - 1][i + 1]
            triangle_row.append(val)
        # append the last 1 to our row:
        triangle_row.append(1)
        result.append(triangle_row)
        counter += 1
    return result


numRows = 5
print(generate(numRows))
