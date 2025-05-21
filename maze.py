import time
from cell import Cell
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()
        if seed is not None:
            random.seed(seed)

    def solve(self):
        self.__solve_r()

    def __create_cells(self):
        self.__cells = [ [ Cell(self._win) for i in range(self._num_rows) ] for j in range(self._num_cols)]
        if self._win is not None:
            for col in range(self._num_cols):
                for row in range(self._num_rows):
                    self.__draw_cell(col,row)
    

    def __draw_cell(self, col, row):
        cell = self.__cells[col][row]
        x1 = self._x1 + self._cell_size_x * col
        y1 = self._y1 + self._cell_size_y * row
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        if self._win is not None:
            cell.draw(x1, y1, x2, y2)
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.025)

    def __break_entrance_and_exit(self):
        top_left_cell = self.__cells[0][0]
        bottom_right_cell = self.__cells[-1][-1]
        top_left_cell.has_top_wall = False
        self.__draw_cell(0,0)
        bottom_right_cell.has_bottom_wall = False
        self.__draw_cell(self._num_cols-1, self._num_rows-1)
        
    def __break_walls_r(self, i, j):
        current_cell = self.__cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []

            index_above= j - 1
            index_below = j + 1
            index_left = i - 1
            index_right = i + 1

            if index_above >= 0:
                cell_above = self.__cells[i][j-1]
                if cell_above.visited == False:
                    to_visit.append([i,j - 1])

            if index_below < self._num_rows:
                cell_below = self.__cells[i][j+1]
                if cell_below.visited == False:
                    to_visit.append([i,j+1])

            if index_left >= 0:
                cell_left = self.__cells[i-1][j]
                if cell_left.visited == False:
                    to_visit.append([i-1, j])

            if index_right < self._num_cols:
                cell_right = self.__cells[i+1][j]
                if cell_right.visited == False:
                    to_visit.append([i+1,j])

            cells_to_visit = len(to_visit)

            if cells_to_visit <= 0:
                self.__draw_cell(i,j) 
                return

            else:
                r_i, r_j = to_visit[random.randrange(0,cells_to_visit,1)]
                chosen_cell = self.__cells[r_i][r_j]
                if chosen_cell._x1 < current_cell._x1:
                    chosen_cell.has_right_wall = False
                    current_cell.has_left_wall = False
                if chosen_cell._x1 > current_cell._x1:
                    current_cell.has_right_wall = False
                    chosen_cell.has_left_wall = False
                if chosen_cell._y1 < current_cell._y1:
                    current_cell.has_top_wall = False
                    chosen_cell.has_bottom_wall = False
                if chosen_cell._y1 > current_cell._y1:
                    current_cell.has_bottom_wall = False
                    chosen_cell.has_top_wall = False
                self.__break_walls_r(r_i, r_j)

    def __reset_cells_visited(self):
        for column in self.__cells:
            for cell in column:
                cell.visited = False

    def __solve_r(self, i=0, j=0):
        end_cell = self.__cells[-1][-1]
        current_cell = self.__cells[i][j]
        self._animate()
        current_cell.visited = True

        if current_cell == end_cell:
            return True
        

        index_above= j - 1
        index_below = j + 1
        index_left = i - 1
        index_right = i + 1

        if index_above >= 0:
            cell_above = self.__cells[i][j-1]
            if cell_above.visited == False and cell_above.has_bottom_wall == False:
                current_cell.draw_move(cell_above) 
                if self.__solve_r(i, j-1):
                    return True
                else: 
                    current_cell.draw_move(cell_above, undo=True)

        if index_below < self._num_rows:
            cell_below = self.__cells[i][j+1]
            if cell_below.visited == False and cell_below.has_top_wall == False:
                current_cell.draw_move(cell_below) 
                if self.__solve_r(i, j+1):
                    return True
                else: 
                    current_cell.draw_move(cell_below, undo=True)

        if index_left >= 0:
            cell_left = self.__cells[i-1][j]
            if cell_left.visited == False and cell_left.has_right_wall == False: 
                current_cell.draw_move(cell_left) 
                if self.__solve_r(i-1, j):
                    return True
                else: 
                    current_cell.draw_move(cell_left, undo=True)

        if index_right < self._num_cols:
            cell_right = self.__cells[i+1][j]
            if cell_right.visited == False and cell_right.has_left_wall == False:
                current_cell.draw_move(cell_right) 
                if self.__solve_r(i+1, j):
                    return True
                else: 
                    current_cell.draw_move(cell_right, undo=True)

        return False







