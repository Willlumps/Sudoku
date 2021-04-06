CC = g++
CPPFLAGS = -g -Wall -std=c++11 -stdlib=libc++

# Python links
PYTHONHEADERS = -I/usr/local/Cellar/python@3.9/3.9.2_4/Frameworks/Python.framework/Versions/3.9/Headers/
PYTHONLIBRARIES = -L/usr/local/Cellar/python@3.9/3.9.2_4/Frameworks/Python.framework/Versions/3.9/lib
PYTHONLIB = -lpython3.9

LIBRARIES = ${PYTHONLIBRARIES} ${PYTHONLIB}
HEADERS = ${PYTHONHEADERS}

# Build target
TARGET = Sudoku

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CPPFLAGS) $(HEADERS) $(LIBRARIES) $(TARGET).cpp -o $(TARGET)

clean:
	$(RM) $(TARGET)
