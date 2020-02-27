import tkinter
from tkinter import *
import sys
import Scraper

gui = tkinter.Tk(className = 'Sudoku')
pixel = tkinter.PhotoImage(width = 1, height = 1)

grid = Scraper.getBoard()

for i in range(9):
    for j in range(9):
        btn = Button(gui, text = grid[i][j],  height = 4, width = 5)
        btn.grid(column=j, row=i)

gui.mainloop()