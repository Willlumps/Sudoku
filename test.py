import numpy as np
from Scraper import getBoard
import tkinter
from tkinter import *
import requests
from bs4 import BeautifulSoup


class Board():

    def __init__(self, board):
        self.board = board

    def puzzle(self):
        return self.board

class GUI(Frame):
    buttons = [[[] for i in range(9)] for j in range(9)]
    currentButton = buttons[0][0]
    buttonText = ""

    def __init__(self, parent, game):
        self.game = game
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initGUI()
        
        

    def __initGUI(self):
        self.parent.title("Sudoku")
        #self.pack(fill=BOTH)
        #self.canvas = Canvas(self, highlightthickness=2, highlightbackground="grey", width=450, height=450)
        #self.canvas.pack(fill=BOTH, side=TOP)
        # self.__dcanvas()
        self.__dboard()

    
    

    def __dboard(self):
        self.pixel = tkinter.PhotoImage(width=1, height=1)
        self.selectedButton = StringVar()
        self.test = StringVar()
        count=0
        print (self.game.puzzle()[1][2])
        for i in range(9):
            for j in range(9):
                btnText = self.game.puzzle()[i][j] if self.game.puzzle()[i][j] != 0 else " "
                if btnText == " ":
                    # btn = Button(self.parent, image=self.pixel, text=btnText, width=50, height=50, compound="left", 
                    #              command=lambda row=j, col=i: self.action(col, row))
                    btn = Radiobutton(self.parent, image=self.pixel, text=btnText, value=count, variable=self.selectedButton, width=50, height=50, 
                                      compound="left", indicatoron=False, command=lambda row=i, col=j: self.getRowCol(col, row))
                else:
                    # btn = Button(self.parent, image=self.pixel, text=btnText, font=("bold"), disabledforeground="#CC6666", width=50, 
                    #               height=50, compound="left", state=DISABLED, command=lambda row=j, col=i: self.action(col, row))
                    btn = Radiobutton(self.parent, image=self.pixel, text=btnText, font=("bold"), value=count, variable=self.selectedButton, 
                                      state=DISABLED, disabledforeground="#CC6666", width=50, height=50, compound="left", indicatoron=False)
                self.buttons[i][j] = btn
                if i == 2 or i == 5:
                    btn.grid(column=j, row=i, pady=(0, 2))
                if j == 2 or j == 5:
                    btn.grid(column=j, row=i, padx=(0, 2))
                else:
                    btn.grid(column=j, row=i)
                count += 1

        one = Button(self.parent, image=self.pixel, text="1", width=50, height=50, compound="left", command=lambda : self.placeShit('1'))
        two = Button(self.parent, image=self.pixel, text="2", width=50, height=50, compound="left", command=lambda : self.placeShit('2'))
        three = Button(self.parent, image=self.pixel, text="3", width=50, height=50, compound="left", command=lambda : self.placeShit('3'))
        four = Button(self.parent, image=self.pixel, text="4", width=50, height=50, compound="left", command=lambda : self.placeShit('4'))
        five = Button(self.parent, image=self.pixel, text="5", width=50, height=50, compound="left", command=lambda : self.placeShit('5'))
        six = Button(self.parent, image=self.pixel, text="6", width=50, height=50, compound="left", command=lambda : self.placeShit('6'))
        seven = Button(self.parent, image=self.pixel, text="7", width=50, height=50, compound="left", command=lambda : self.placeShit('7'))
        eight = Button(self.parent, image=self.pixel, text="8", width=50, height=50, compound="left", command=lambda : self.placeShit('8'))
        nine = Button(self.parent, image=self.pixel, text="9", width=50, height=50, compound="left", command=lambda : self.placeShit('9'))

        one.grid(column=0, row=9, pady=(20, 0))
        two.grid(column=1, row=9, pady=(20, 0))
        one.grid(column=0, row=9, pady=(20, 0))
        two.grid(column=1, row=9, pady=(20, 0))
        three.grid(column=2, row=9, pady=(20, 0))
        four.grid(column=3, row=9, pady=(20, 0))
        five.grid(column=4, row=9, pady=(20, 0))
        six.grid(column=5, row=9, pady=(20, 0))
        seven.grid(column=6, row=9, pady=(20, 0))
        eight.grid(column=7, row=9, pady=(20, 0))
        nine.grid(column=8, row=9, pady=(20, 0))

    def getRowCol(self, row, col):
        self.currentButton = self.buttons[col][row]
        print(self.selectedButton.get())
    def placeShit(self, tex):
        # self.selectedButton
        self.currentButton.config(text=tex)
    



    def possiblePlay(self, row, col, num):
        for i in range(9):
            if (self.grid[row][i] == num):
                return False
        for i in range(9):
            if (self.grid[i][col] == num):
                return False

        for i in range(3):
            for j in range(3):
                if (self.grid[((row//3) * 3) + i][((col//3) * 3) + j] == num):
                    return False
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if (self.grid[row][col] == 0):
                    for num in range(1, 10):
                        if (self.possiblePlay(row, col, num)):
                            self.grid[row][col] = num
                            self.solve()
                            self.grid[row][col] = 0
                    return
        print("---------------------------------------------")
        # print(np.matrix(self.grid))


if __name__ == '__main__':

    game = Board(getBoard())
    root = Tk()
    root.config(background="black")
    gui = GUI(root, game)
    
    root.mainloop()