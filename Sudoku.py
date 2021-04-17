import numpy as np
from Scraper import getSudokuBoard
import tkinter
from tkinter import *
from tkinter import messagebox
import copy


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


class GUI(Frame):

    """ The main GUI for our Sudoku board
    Displays the board as well as all action buttons used in gameplay
    Attributes:
        game: The board that stores the state of the current game
        parent: The Frame the gui resides in
    """
    # Array for holding each Button on our game board
    buttons = [[[] for i in range(9)] for j in range(9)]
    # Stores the currently selected button
    currentButton = buttons[0][0]
    # Placeholders to hold the row and column of the selected button
    ro = 0
    co = 0

    def __init__(self, parent):
        """ Initializes a GUI with a drawn game board"""
        self.game = Board(getSudokuBoard())
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initGUI()

    def __initGUI(self):
        """ Initializs the board aspect of our GUI """
        self.parent.title("Sudoku")
        self.__dboard()

    def __dboard(self):
        """ Initializes and sets up each game tile with respect to the 
        starting game board
        """
        # 1x1 pixel image used to create uniform button sizes
        self.pixel = tkinter.PhotoImage(width=1, height=1)
        # StringVar used to distinguish which cell is selected
        self.selectedButton = StringVar()

        # Count variable used to assign each cell a unique value.
        count = 0

        # Creates a 2D Array of game cells and adds them to the GUI in a grid layout
        for i in range(9):
            for j in range(9):
                # If the value of the cell is 0 (Empty), display no value, 
                # otherwise displays the numeric value from 1 through 9
                # A non empty cell indicates that it was default board cell and should
                # be immutable. These game cells are indicated by a red font and disabled state
                btnText = self.game.getBoard202()[i][j] if self.game.getBoard202()[i][j] != 0 else " "
                if btnText == " ":
                    btn = Radiobutton(self.parent, image=self.pixel, text=btnText, font=("bold"), value=count,
                                      variable=self.selectedButton, width=50, height=50,
                                      compound="left", indicatoron=False, bg="#D0D8E3",
                                      command=lambda row=i, col=j: self.getRowCol(col, row))
                else:
                    btn = Radiobutton(self.parent, image=self.pixel, text=btnText, font=("bold"), value=count,
                                      variable=self.selectedButton,
                                      state=DISABLED, disabledforeground="#CC6666", width=50, height=50,
                                      compound="left", indicatoron=False, bg="#D0D8E3")
                self.buttons[i][j] = btn

                # Adds padding around certain cells simulate a divided nature
                # Between each 3x3 grid.
                if i == 2 or i == 5:
                    btn.grid(column=j, row=i, pady=(0, 2))
                if j == 2 or j == 5:
                    btn.grid(column=j, row=i, padx=(0, 2))
                else:
                    btn.grid(column=j, row=i)
                count += 1

        # Creates all of our action buttons used during gameplay. 
        one = Button(self.parent, image=self.pixel, text="1", font=("bold"), width=52, height=50, compound="left",
                     bg="#A1B2C7", command=lambda: self.placeCell('1'))
        two = Button(self.parent, image=self.pixel, text="2", font=("bold"), width=52, height=50, compound="left",
                     bg="#A1B2C7", command=lambda: self.placeCell('2'))
        three = Button(self.parent, image=self.pixel, text="3", font=("bold"), width=52, height=50, compound="left",
                       bg="#A1B2C7", command=lambda: self.placeCell('3'))
        four = Button(self.parent, image=self.pixel, text="4", font=("bold"), width=52, height=50, compound="left",
                      bg="#A1B2C7", command=lambda: self.placeCell('4'))
        five = Button(self.parent, image=self.pixel, text="5", font=("bold"), width=52, height=50, compound="left",
                      bg="#A1B2C7", command=lambda: self.placeCell('5'))
        six = Button(self.parent, image=self.pixel, text="6", font=("bold"), width=52, height=50, compound="left",
                     bg="#A1B2C7", command=lambda: self.placeCell('6'))
        seven = Button(self.parent, image=self.pixel, text="7", font=("bold"), width=52, height=50, compound="left",
                       bg="#A1B2C7", command=lambda: self.placeCell('7'))
        eight = Button(self.parent, image=self.pixel, text="8", font=("bold"), width=52, height=50, compound="left",
                       bg="#A1B2C7", command=lambda: self.placeCell('8'))
        nine = Button(self.parent, image=self.pixel, text="9", font=("bold"), width=52, height=50, compound="left",
                      bg="#A1B2C7", command=lambda: self.placeCell('9'))
        solve = Button(self.parent, image=self.pixel, text="Solve", font=("bold"), width=110, height=50, bg="#A1B2C7",
                       compound="left", command=lambda: self.paintSolve())
        reset = Button(self.parent, image=self.pixel, text="Reset Board", font=("bold"), width=115, height=50, 
                       bg="#A1B2C7", compound="left", command=lambda: self.reset())
        clear = Button(self.parent, image=self.pixel, text="Clear", font=("bold"), width=52, height=50, bg="#A1B2C7",
                       compound="left", command=lambda: self.placeCell(' '))
        newGame = Button(self.parent, image=self.pixel, text="New Game", font=("bold"), width=115, height=50, 
                         bg="#A1B2C7", compound="left", command=lambda: self.newBoard(self.parent))
        quitGame = Button(self.parent, image=self.pixel, text="Quit", font=("bold"), width=112, height=50, bg="#A1B2C7",
                       compound="left", command=lambda: self.quit())
        # Adds the action buttons below the game board
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
        solve.grid(column=0, row=11, columnspan=2)
        reset.grid(column=2,row=11, columnspan=2)
        clear.grid(column=4, row=11)
        newGame.grid(column=5, row=11, columnspan=2)
        quitGame.grid(column=7, row=11, columnspan=2)

    def getRowCol(self, row, col):
        """ Stores the cell information of the currently selected cell
        for later use in the placeCell() function
        """
        self.currentButton = self.buttons[col][row]
        self.ro = row
        self.co = col

    def placeCell(self, tex):
        """ Updates the currently selected cell with the corresponding of the action 
        button that was pressed. 
        """

        # Updates the selected cell with the passed text value, in this case
        # it corresponds to the value of the action button that was pressed.
        self.currentButton.config(text=tex)
        # Updates the game board as well
        self.game.getBoard202()[self.co][self.ro] = int(tex) if tex != ' ' else tex
        # Checks if the last play was a winning move. 
        if self.game.checkWin():
            print("You won or something, I guess")
            self.onWin()

    def paintSolve(self):
        """ Updates the game board with the solved board """

        # Sets the game board back to the starting point.
        for i in range(9):
            for j in range(9):
                self.game.board[i][j] = self.game.resetBoard[i][j]

        # Solves the puzzle and prints the solved board
        print("solving...")
        self.game.solve()
        print('solved:')
        print(np.matrix(self.game.solvedBoard))
        
        # Updates each game cell to the correct solved value. 
        for i in range(9):
            for j in range(9):
                self.buttons[i][j].deselect()
                self.buttons[i][j].config(text=self.game.solvedBoard[i][j], state=DISABLED)

    def reset(self):
        """ Resets the game board to the default starting point """
        for i in range(9):
            for j in range(9):
                self.buttons[i][j].deselect()
                self.buttons[i][j].config(text=self.game.resetBoard[i][j] if 
                                          self.game.resetBoard[i][j] != 0 else " ", 
                                          state=NORMAL if self.buttons[i][j].cget("disabledforeground") 
                                          != "#CC6666" else DISABLED)

    def newBoard(self, parent):
        """ Fetches a new game board and reinitilizes the GUI to reflect the new game board """
        
        # Prompts the user if they are sure they would like to start a new game. 
        newBoardMessage = messagebox.askquestion("Warning", "This will abandon your current game and "+
                "all progress will be lost, continue?")
        if (newBoardMessage == 'yes'):
            self.__init__(parent)

        

    def onWin(self):
        """ Handles when the user has won the game. Creates a popup indicating
        that they have won and offers them the option to start a new game or quit.
        """
        winMessage = Toplevel(root)
        winMessage.title('Winner!')
        winMessage.geometry("200x75")
        winLabel = Label(winMessage, text='Congrats, you\'ve won!!').pack()
        Button(winMessage, text="New Game", command=lambda: self.newBoard(self.parent)).pack()
        Button(winMessage, text="Quit", command=lambda: self.quit()).pack()
        

if __name__ == '__main__':
    root = Tk()
    root.config(background="black")
    gui = GUI(root)

    root.mainloop()
