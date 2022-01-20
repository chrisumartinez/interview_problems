from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # in order to be a valid sudoku, it must pass 3 requirements:
    # must pass that the row is correct
    # must pass that the column is correct
    # each 3x3 box must be valid sudoku√

    def rowCheck(row):
        num_set = set()
        for i in range(len(row)):
            if row[i] in num_set and row[i] != ".":
                return False
            else:
                num_set.add(row[i])
        return True

    def columnCheck(board):
        # use validate row to validate column:
        for column_index in range(9):
            column = []
            for row_index in range(9):
                column.append(board[row_index][column_index])
            if not rowCheck(column):
                return False
        return True

    def littleBoxCheck(board):
        # check if the little boxes are valid:
        for row_index in range(0, 7, 3):
            for column_index in range(0, 7, 3):
                box = [
                    board[row_index + 0][column_index + 0],
                    board[row_index + 0][column_index + 1],
                    board[row_index + 0][column_index + 2],
                    board[row_index + 1][column_index + 0],
                    board[row_index + 1][column_index + 1],
                    board[row_index + 1][column_index + 2],
                    board[row_index + 2][column_index + 0],
                    board[row_index + 2][column_index + 1],
                    board[row_index + 2][column_index + 2],
                ]

                if not rowCheck(box):
                    return False
        return True

    # check every row to make sure it passes rowCheck:
    for row in board:
        if not rowCheck(row):
            return False
    # now make sure it passes each columnCheck:
    return columnCheck(board) and littleBoxCheck(board)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(isValidSudoku(board))  # true
print(isValidSudoku(board2))  # false
