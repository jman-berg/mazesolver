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
        
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color) 

    def wait_for_close(self):
        self.__isrunning = True
        while self.__isrunning:
            self.redraw()

    def close(self):
        self.__isrunning = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas,fill_color):
        canvas.create_line(
        self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = fill_color, width=2
    )

class Cell:
    def __init__(
        self,
        top_left_point,
        bottom_right_point,
        win,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_top_wall = has_top_wall
        self._x1 = top_left_point.x
        self._y1 = top_left_point.y
        self._x2 = bottom_right_point.x
        self._y2 = bottom_right_point.y
        self._win = win

    def draw(self):
        point_left_wall_top = Point(self._x1, self._y1)
        point_left_wall_bottom = Point(self._x1, self._y2)
        point_right_wall_bottom = Point(self._x2, self._y2)
        point_right_wall_top = Point(self._x2, self._y1)

        line_left = Line(point_left_wall_top, point_left_wall_bottom)
        line_top = Line(point_left_wall_top, point_right_wall_top)
        line_bottom = Line(point_right_wall_bottom, point_left_wall_bottom)
        line_right = Line(point_right_wall_top, point_right_wall_bottom)
        
        if self.has_top_wall:
            self._win.draw_line(line_top, "blue")
        if self.has_bottom_wall:
            self._win.draw_line(line_bottom, "blue")
        if self.has_left_wall:
            self._win.draw_line(line_left, "blue")
        if self.has_right_wall:
            self._win.draw_line(line_right, "blue")




def main():
    win = Window(800,600)
    point1 = Point(30,30)
    point2 = Point(50, 20)
    cell = Cell(
        has_left_wall=True,
        has_right_wall=False,
        has_bottom_wall=True,
        has_top_wall=True,
        top_left_point=point1, bottom_right_point=point2, win=win)
    cell.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()



