import requests
from bs4 import BeautifulSoup

def getSudokuBoard():
    url = 'https://nine.websudoku.com/?level=4'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #grid = []
    board = ""

    results = soup.find("table", id="puzzle_grid")

    for table in results.findAll("tr"):
        
        row = []
        for test in table.findAll("input"):

            if (test.get("maxlength") == "1"):
                #row.append(0)
                board += "0 "
            else:
                #row.append(int(test.get("value")))
                board += test.get("value") + " "
        #grid.append(row)
    f = open("board", 'w')
    f.write(board)
    #return grid
          

getSudokuBoard()
