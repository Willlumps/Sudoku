import requests
from bs4 import BeautifulSoup
import numpy as np

url = 'https://nine.websudoku.com/?level=4&set_id=8362066110'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

def getBoard():
    
    grid = []

    results = soup.find("table", id="puzzle_grid")

    for table in results.findAll("tr"):
        
        row = []
        for test in table.findAll("input"):

            if (test.get("maxlength") == "1"):
                row.append(None)
            else:
                row.append(int(test.get("value")))
        grid.append(row)

    print(np.matrix(grid))
    return grid
          
# getBoard()