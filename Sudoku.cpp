#include <Python/Python.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  Py_Initialize();
  
  FILE *fp;
  char buffer[1024];
  fp = fopen("Scraper.py", "r");
  PyRun_SimpleFile(fp, "Scraper.py");
  Py_Finalize();
  return 0;
}
