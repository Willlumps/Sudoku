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

    def __dcanvas(self):
        spacing = 50
        for i in range(9):
            lineColor = "grey" if i % 3 == 0 else "blue"
            lineThickness = 2 if i % 3 == 0 else 1

            # Vertical board lines
            x1 = i * spacing
            y1 = 0
            x2 = i * spacing
            y2 = 500
            self.canvas.create_line(x1, y1, x2, y2, fill=lineColor, width=lineThickness)

            # Horizontal board lines
            x1 = 0
            y1 = i * spacing
            x2 = 500
            y2 = i * spacing
            self.canvas.create_line(x1, y1, x2, y2, fill=lineColor, width=lineThickness)

    def __dboard(self):
        self.pixel = tkinter.PhotoImage(width=1, height=1)
        rowInc = 0
        colInc = 0
        for h in range(10):
            for i in range(3):
                for j in range(3):
                    
                    btn = Button(self.parent, image=self.pixel, text=str(h), width=50, height=50, compound="left")
                    if j == 2 and h < 6:
                        btn.grid(column=i + colInc, row=j + rowInc, pady=(0, 2))
                    if i == 2 and h % 3 != 0:
                        btn.grid(column=i + colInc, row=j + rowInc, padx=(0, 2))
                    else:
                        btn.grid(column=i + colInc, row=j + rowInc)
            
            if h == 3 or h == 6:
                rowInc += 3
            if h % 3 == 0:
                colInc = 0
            else:
                colInc += 3

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