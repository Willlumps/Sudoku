import numpy as np

grid = [[6, 1, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 6, 0, 4, 0],
        [2, 0, 0, 0, 1, 7, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 7, 6],
        [4, 0, 9, 0, 0, 0, 2, 0, 1],
        [5, 2, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 4, 7, 0, 0, 0, 5],
        [0, 8, 0, 3, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 1, 3]]

def possiblePlay(row, col, num):
    for i in range(9):
        if (grid[row][i] == num):
            return False
    for i in range(9):
        if (grid[i][col] == num):
            return False

    for i in range(3):
        for j in range(3):
            if (grid[((row//3) * 3) + i][((col//3) * 3) + j] == num):
                return False
    return True

def solve():
    for row in range(9):
        for col in range(9):
            if (grid[row][col] == 0):
                for num in range(1, 10):
                    if (possiblePlay(row, col, num)):
                        grid[row][col] = num
                        solve()
                        grid[row][col] = 0
                return
    print(np.matrix(grid))

solve()

#test haha