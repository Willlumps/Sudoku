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
        for i in range(9):
            for j in range(9):
                btnText = self.game.puzzle()[j][i] if self.game.puzzle()[j][i] != 0 else " "
                btn = Button(self.parent, image=self.pixel, text=btnText, width=50, height=50, compound="left")
                if j == 2 or j == 5:
                    btn.grid(column=i, row=j, pady=(0, 2))
                if i == 2 or i == 5:
                    btn.grid(column=i, row=j, padx=(0, 2))
                else:
                    btn.grid(column=i, row=j)
                # cell = self.game.puzzle()[j][i]
                # if cell != 0:
                #     row = (i * 50) + 25
                #     col = (j * 50) + 25
                #     self.canvas.create_text(row, col, text=cell, tags="numbers")
        

    # def __btnTest(self):

   
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