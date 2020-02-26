import tkinter
from tkinter import *
import sys

print (sys.version)


gui = tkinter.Tk(className = 'Sudoku')
pixel = tkinter.PhotoImage(width = 1, height = 1)
#gui.geometry('500x500')


for i in range(9):
    for j in range(9):
        btn = Button(gui, text = "", image = pixel, height = 50, width = 50)
        btn.grid(column=j, row=i)
gui.mainloop()