import numpy as np
from Scraper import getSudokuBoard
import tkinter
from tkinter import *
from tkinter import messagebox
import copy


class Board():

    def __init__(self, board):
        self.board = board
        self.resetBoard = board
        self.solvedBoard = None

    def possiblePlay(self, board, row, col, num):
        for i in range(9):
            if (board[row][i] == num):
                return False
        for i in range(9):
            if (board[i][col] == num):
                return False

        for i in range(3):
            for j in range(3):
                if (board[((row // 3) * 3) + i][((col // 3) * 3) + j] == num):
                    return False
        return True

    # ----------------------

    def solve(self):
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
        if self.__checkRows() and self.__checkCols() and self.__checkSquares():
            return True
        return False

    # ----------------------

    def __checkRows(self):
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


class GUI(Frame):
    buttons = [[[] for i in range(9)] for j in range(9)]
    currentButton = buttons[0][0]
    buttonText = ""
    ro = 0
    co = 0

    def __init__(self, parent):
        self.game = Board(getSudokuBoard())
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initGUI()

    def __initGUI(self):
        self.parent.title("Sudoku")
        self.__dboard()

    def __dboard(self):
        self.pixel = tkinter.PhotoImage(width=1, height=1)
        self.selectedButton = StringVar()
        self.test = StringVar()
        count = 0
        for i in range(9):
            for j in range(9):
                btnText = self.game.getBoard202()[i][j] if self.game.getBoard202()[i][j] != 0 else " "
                if btnText == " ":
                    # btn = Button(self.parent, image=self.pixel, text=btnText, width=50, height=50, compound="left", 
                    #              command=lambda row=j, col=i: self.action(col, row))
                    btn = Radiobutton(self.parent, image=self.pixel, text=btnText, font=("bold"), value=count,
                                      variable=self.selectedButton, width=50, height=50,
                                      compound="left", indicatoron=False, bg="#D0D8E3",
                                      command=lambda row=i, col=j: self.getRowCol(col, row))
                else:
                    # btn = Button(self.parent, image=self.pixel, text=btnText, font=("bold"), disabledforeground="#CC6666", width=50, 
                    #               height=50, compound="left", state=DISABLED, command=lambda row=j, col=i: self.action(col, row))
                    btn = Radiobutton(self.parent, image=self.pixel, text=btnText, font=("bold"), value=count,
                                      variable=self.selectedButton,
                                      state=DISABLED, disabledforeground="#CC6666", width=50, height=50,
                                      compound="left", indicatoron=False, bg="#D0D8E3")
                self.buttons[i][j] = btn
                if i == 2 or i == 5:
                    btn.grid(column=j, row=i, pady=(0, 2))
                if j == 2 or j == 5:
                    btn.grid(column=j, row=i, padx=(0, 2))
                else:
                    btn.grid(column=j, row=i)
                count += 1

        one = Button(self.parent, image=self.pixel, text="1", font=("bold"), width=52, height=50, compound="left",
                     bg="#A1B2C7", command=lambda: self.placeShit('1'))
        two = Button(self.parent, image=self.pixel, text="2", font=("bold"), width=52, height=50, compound="left",
                     bg="#A1B2C7", command=lambda: self.placeShit('2'))
        three = Button(self.parent, image=self.pixel, text="3", font=("bold"), width=52, height=50, compound="left",
                       bg="#A1B2C7", command=lambda: self.placeShit('3'))
        four = Button(self.parent, image=self.pixel, text="4", font=("bold"), width=52, height=50, compound="left",
                      bg="#A1B2C7", command=lambda: self.placeShit('4'))
        five = Button(self.parent, image=self.pixel, text="5", font=("bold"), width=52, height=50, compound="left",
                      bg="#A1B2C7", command=lambda: self.placeShit('5'))
        six = Button(self.parent, image=self.pixel, text="6", font=("bold"), width=52, height=50, compound="left",
                     bg="#A1B2C7", command=lambda: self.placeShit('6'))
        seven = Button(self.parent, image=self.pixel, text="7", font=("bold"), width=52, height=50, compound="left",
                       bg="#A1B2C7", command=lambda: self.placeShit('7'))
        eight = Button(self.parent, image=self.pixel, text="8", font=("bold"), width=52, height=50, compound="left",
                       bg="#A1B2C7", command=lambda: self.placeShit('8'))
        nine = Button(self.parent, image=self.pixel, text="9", font=("bold"), width=52, height=50, compound="left",
                      bg="#A1B2C7", command=lambda: self.placeShit('9'))
        solve = Button(self.parent, image=self.pixel, text="Solve", font=("bold"), width=52, height=50, bg="#A1B2C7",
                       compound="left", command=self.paintSolve())

        one.grid(column=0, row=10, pady=(3, 0))
        two.grid(column=1, row=10, pady=(3, 0))
        one.grid(column=0, row=10, pady=(3, 0))
        two.grid(column=1, row=10, pady=(3, 0))
        three.grid(column=2, row=10, pady=(3, 0))
        four.grid(column=3, row=10, pady=(3, 0))
        five.grid(column=4, row=10, pady=(3, 0))
        six.grid(column=5, row=10, pady=(3, 0))
        seven.grid(column=6, row=10, pady=(3, 0))
        eight.grid(column=7, row=10, pady=(3, 0))
        nine.grid(column=8, row=10, pady=(3, 0))
        solve.grid(column=0, row=11)

    def getRowCol(self, row, col):
        self.currentButton = self.buttons[col][row]
        self.ro = row
        self.co = col

    def placeShit(self, tex):
        self.currentButton.config(text=tex)
        self.game.getBoard202()[self.co][self.ro] = int(tex)
        if self.game.checkWin():
            print("You won or something, I guess")
        # print(np.matrix(self.game.getBoard()))

    def paintSolve(self):

        # ill leave this portion for you to write
        print("solving...")
        self.game.solve()
        print('solved:')
        print(np.matrix(self.game.solvedBoard))


if __name__ == '__main__':
    # game = Board(getBoard())
    root = Tk()
    root.config(background="black")
    # gui = GUI(root, game)
    gui = GUI(root)

    root.mainloop()

# TODO CLEAR BOARD BUTTON, NEW GAME OPTION, SOLVE OPTION, POP-UP ON WIN - QUIT OR NEW GAME
# deepcopy 201 46
