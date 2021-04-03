from Scraper import getSudokuBoard
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys


class MainWidget(QWidget):

  def __init__(self):
    super().__init__()
    self.button_show()

  def button_show(self):
    button = QPushButton("CLICK ME!!!", self)
    button1= QPushButton("CLICK ME!!!", self)
    button.resize(200, 60)
    button1.resize(400, 60)
    button.clicked.connect(self.on_click)
    button1.clicked.connect(self.on_click)
    

  def on_click(self):
    print("USER CLICKED ME")

def main():
  app = QApplication(sys.argv)

  widget = MainWidget()
  widget.resize(640, 480)
  widget.setWindowTitle("Sudoku")
  widget.show()

  app.exec_()

if __name__ == '__main__':
  main()
