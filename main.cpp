#include <QApplication>
#include <QWidget>
#include <iostream>

int main(int argc, char *argv[]) {

  QApplication app(argc, argv);

  QWidget window;

  window.resize(250, 250);
  window.setWindowTitle("Simple example");
  window.show();

  return app.exec();
}
