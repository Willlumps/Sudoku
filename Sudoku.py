import numpy as np
from Scraper import getSudokuBoard
import copy
import pygame
import sys


class Board():   
    # Stores the current state of the Sudoku board and handles all logic
    # used in the game itself

    def __init__(self, board):
        self.board = board
        self.resetBoard = copy.deepcopy(board)
        self.solvedBoard = None

    def possiblePlay(self, board, row, col, num):
        """ Returns True if this cell is a valid play. For example if the row,
        column, or 3x3 game cell does not contain another instance of the passed
        num argument.
        """

        # Checks The columns
        for i in range(9):
            if (board[row][i] == num):
                return False
        # Checks the rows
        for i in range(9):
            if (board[i][col] == num):
                return False
        # Checks the 3x3 cell
        for i in range(3):
            for j in range(3):
                if (board[((row // 3) * 3) + i][((col // 3) * 3) + j] == num):
                    return False
        return True

    # ----------------------

    def solve(self):
        """ Solves the current game board"""
        # If the board hasn't been solved yet, creates a copy of the board
        # and solves it, returning the solved board for future use. 
        if self.solvedBoard is None:
            the_board = copy.deepcopy(self.board)
            self.solveSolution(the_board)
            self.solvedBoard = the_board

        return self.solvedBoard

    # ----------------------
    # ----------------------

    # took the solution from stanford
    # https://see.stanford.edu/Course/CS106B/149

    # find any unassigned location and return it
    def find_unassigned(self, board):
        if board is not None:
            for row in range(9):
                for col in range(9):
                    if (board[row][col] == 0):
                        # here we just store it into an array
                        first = []
                        first.append(row)
                        first.append(col)
                        return first
        return None

    # ----------------------

    def solveSolution(self, the_board):

        res = self.find_unassigned(the_board)
        row = 0
        col = 0

        # based on line 53-56, we use the similar format to pull out the row,col
        if res is not None:
            row = res[0]
            col = res[1]

            # solution options
            for num in range(1, 10):
                # changed the method to take any board, instead of self.board
                if self.possiblePlay(the_board, row, col, num):
                    the_board[row][col] = num
                    if (self.solveSolution(the_board)):
                        return True
                    # undo and try again
                    the_board[row][col] = 0
            # this allows for backtracking from early decisions
            return False
        else:
            # early exit, in case we have assigned all positions
            return True

    # ----------------------
    # ----------------------

    def getBoard202(self):
        return self.board

    # ----------------------

    def checkWin(self):
        """ Checks the state of the board for a win """
        if self.__checkRows() and self.__checkCols() and self.__checkSquares():
            return True
        return False

    # ----------------------

    def __checkRows(self):
        # Iterates through each row looking for duplicate numbers
        # if none are found returns true, otherwise false
        count = 0
        for i in range(9):
            if len(self.board[i]) != len(set(self.board[i])):
                return False
            if not 0 in self.board[i]:
                count += 1
        if count == 9:
            return True

    # ----------------------

    def __checkCols(self):
        # Iterates through each column looking for duplicate numbers
        # if none are found returns true, otherwise false
        count = 0
        for i in range(9):
            columns = []
            for j in range(9):
                columns.append(self.board[j][i])
            if len(columns) != len(set(columns)):
                return False
            if not 0 in columns:
                count += 1
        if count == 9:
            return True

    def __checkSquares(self):
        # Iterates through each 3x3 cell looking for duplicate numbers
        # if none are found returns true, otherwise false
        count = 0
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if self.__singleSquare(i, j) == False:
                    return False
                else:
                    count += 1
        if count == 9:
            return True

    def __singleSquare(self, row, col):
        # Iterates through a single 3x3 cell looking for duplicate numbers
        # if none are found returns true, otherwise false
        count = 0
        squares = []
        for i in range(3):
            for j in range(3):
                squares.append(self.board[i + row][j + col])
        if len(squares) != len(set(squares)):
            return False
        if not 0 in squares:
            count += 1
        if count == 1:
            return True
        else:
            return False


#class GUI(Frame):
#
#    def __init__(self, parent):
#
#    def __initGUI(self):
#
#    def __dboard(self):
#
#    def getRowCol(self, row, col):
#
#    def placeCell(self, tex):
#
#    def paintSolve(self):
#
#    def reset(self):
#
#    def newBoard(self, parent):
#
#    def onWin(self):
        

if __name__ == '__main__':
  pygame.init()
  pygame.display.set_caption("dicks")

  screen = pygame.display.set_mode((240, 180))

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
