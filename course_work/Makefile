# compilator use
CC =g++
# flags for compile
CFLAGS = -Wall
GLFWFLAGS =-lglfw3 -lGL -lX11 -lpthread -lXrandr -lXi
GLADFLAGS = -ldl
# standart use
CXXFLAGS =-std=c++14

TARGET =pendulum

SRC_DIR =./src/
OBJ_DIR = ./obj/

SRC_FILES := $(wildcard $(SRC_DIR)*.cpp $(SRC_DIR)*.c)
OBJ_FILES := $(patsubst $(SRC_DIR)%.cpp,$(OBJ_DIR)%.o,$(SRC_FILES))

# сделать отдельную папку для объектников или их тоже в build, тогкда как?

all : $(TARGET)

$(TARGET) : $(OBJ_FILES)
	$(CC) -o $@  $^ $(GLFWFLAGS) $(GLADFLAGS)

$(OBJ_DIR)%.o : $(SRC_DIR)%.cpp
	$(CC) $(CFLAGS) $(CXXFLAGS) -c -o $@  $<

clean :
	rm -rf  $(OBJ_DIR)*.o  $(TARGET)
