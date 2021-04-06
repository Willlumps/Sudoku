#include <Python.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>

class Sudoku {
  int board[9][9];
  public:
    Sudoku();
    ~Sudoku();

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
  std::getline(infile, line);
  std::cout << line << std::endl;
}

int main(int argc, char *argv[]) {
  Py_Initialize();
  FILE *fp;
  fp = fopen("Scraper.py", "r");
  PyRun_SimpleFile(fp, "Scraper.py");
  Py_Finalize();

  Sudoku *game = new Sudoku();
  return 0;
}
