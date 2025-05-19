import time
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [ [ Cell(self._win) for i in range(self._num_rows) ] for j in range(self._num_cols)]
        if self._win is not None:
            for col in range(self._num_cols):
                for row in range(self._num_rows):
                    self.__draw_cell(col,row)
    

    def __draw_cell(self, col, row):
        cell = self.__cells[col][row]
        x1 = self._cell_size_x * col
        y1 = self._cell_size_y * row
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        if self._win is not None:
            cell.draw(x1, y1, x2, y2)
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

