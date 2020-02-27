import numpy as np
import Scraper

grid = Scraper.getBoard()

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
    print("---------------------------------------------")
    print(np.matrix(grid))

solve()

#test haha