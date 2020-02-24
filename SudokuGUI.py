import tkinter
from tkinter import *
import sys

print (sys.version)


gui = tkinter.Tk(className = 'Sudoku')
#gui.geometry('500x500')


for i in range(9):
    for j in range(9):
        btn = Button(gui, height = 4, width = 5)
        btn.grid(column=j, row=i)
gui.mainloop()