from graphics import Window, Line, Point


class Cell:
    def __init__(
        self,
        win=None,
    ):
        self.has_left_wall = True 
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        point_left_wall_top = Point(self._x1, self._y1)
        point_left_wall_bottom = Point(self._x1, self._y2)
        point_right_wall_bottom = Point(self._x2, self._y2)
        point_right_wall_top = Point(self._x2, self._y1)

        line_left = Line(point_left_wall_top, point_left_wall_bottom)
        line_top = Line(point_left_wall_top, point_right_wall_top)
        line_bottom = Line(point_right_wall_bottom, point_left_wall_bottom)
        line_right = Line(point_right_wall_top, point_right_wall_bottom)

        if self._win is not None:
        
            if self.has_top_wall:
                self._win.draw_line(line_top, "blue")
            if self.has_bottom_wall:
                self._win.draw_line(line_bottom, "blue")
            if self.has_left_wall:
                self._win.draw_line(line_left, "blue")
            if self.has_right_wall:
                self._win.draw_line(line_right, "blue")

    def draw_move(self, to_cell, undo=False):
        self._start_x = (self._x1 + self._x2) / 2
        self._start_y = (self._y1 + self._y2) / 2
        self._end_x = (to_cell._x1 + to_cell._x2) /2
        self._end_y = (to_cell._y1 + to_cell._y2) / 2
        self.undo = undo
        if undo:
            color = "gray"
        else:
            color = "red"

        point_start = Point(self._start_x, self._start_y)
        point_end = Point(self._end_x, self._end_y)

        line = Line(point_start, point_end)

        if self._win is not None:
            self._win.draw_line(line, color )

