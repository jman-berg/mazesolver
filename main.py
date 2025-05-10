from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isrunning = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isrunning = True
        while self.__isrunning:
            self.redraw()

    def close(self):
        self.__isrunning = False

def main():
    win = Window(800,600)
    win.wait_for_close()


if __name__ == "__main__":
    main()



