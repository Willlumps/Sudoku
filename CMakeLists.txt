cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} \
-g \
-Wall \
-std=c++11 \
-stdlib=libc++ \
-I/usr/local/Cellar/python@3.9/3.9.2_4/Frameworks/Python.framework/Versions/3.9/Headers/ \
-L/usr/local/Cellar/python@3.9/3.9.2_4/Frameworks/Python.framework/Versions/3.9/lib"
)
# Set the project name
project(Sudoku)

# Add the executable
add_executable(
  Sudoku 
  Sudoku.cpp
)

# Specify teh C++ Standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
