from tkinter import Tk, BOTH, Canvas
from cell import Cell
from graphics import Window, Line, Point
from maze import Maze







def main():
    win = Window(800,600)
    maze = Maze(0,0, 10,10,50, 20, win)
    print(maze._Maze__cells)
    


    win.wait_for_close()


if __name__ == "__main__":
    main()



