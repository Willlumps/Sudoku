#include <Python.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

class Sudoku {
  // TODO Make this dynamic so it's easier to throw around?
  //int board[9][9];
  std::vector<std::vector<int>> board = std::vector<std::vector<int>>(9, std::vector<int>(9));

  public:
    Sudoku();
    ~Sudoku();
    std::vector<std::vector<int>>* getBoard();
    void solve();

  private:
    char* readFile(const char* source);
    void initializeBoard();

};

Sudoku::Sudoku() {
  initializeBoard(); 
}

void Sudoku::initializeBoard() {
  std::ifstream infile("board");
  std::string line;

  // Read file
  if (!std::getline(infile, line)) {
    fprintf(stderr, "Error: getline failed");
    exit(1);
  }
  std::cout << line << std::endl;
 
  // Populate game board
  int count = 0;
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      this->board[i][j] = stoi(line.substr(count, 1));
      count++;
    }
  }

  //for (int i = 0; i < 9; i++) {
  //  for (int j = 0; j < 9; j++) {
  //    std::cout << std::to_string(this->board[i][j]) << " ";
  //  }
  //  std::cout << std::endl;
  //}
}
std::vector<std::vector<int>>* Sudoku::getBoard() {
  return &this->board;
}

int main(int argc, char *argv[]) {
  /*
  Py_Initialize();
  FILE *fp;
  fp = fopen("Scraper.py", "r");
  PyRun_SimpleFile(fp, "Scraper.py");
  Py_Finalize();
  */

  Sudoku *game = new Sudoku();
  return 0;
}
