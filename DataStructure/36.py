from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    row, column = [[0] * 9 for _ in range(9)], [[0] * 9 for _ in range(9)]
    matrix = [[[0] * 3 for _ in range(3)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            char = board[i][j]
            if char != '.':
                index = int(char) - 1
                row[i][index] += 1
                column[index][j] += 1
                matrix[int(i / 3)][int(j / 3)][index] += 1
                if row[i][index] > 1 or column[index][j] > 1 or matrix[int(i / 3)][int(j / 3)][index] > 1:
                    return False

    return True


if __name__ == '__main__':
    print(isValidSudoku("aaa"))
