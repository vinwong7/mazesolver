from cell import Cell
import time
import random

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win = None,
                 seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            self.seed = random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        cell_column = []
        for i in range(self.num_rows):
            cell_column.append(Cell(self.win))
        for j in range(self.num_cols):
            self._cells.append(cell_column)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        current_cell_x1 = self.x1 + (self.cell_size_x * i)
        current_cell_y1 = self.y1 + (self.cell_size_y * j)
        current_cell_x2 = current_cell_x1 + self.cell_size_x
        current_cell_y2 = current_cell_y1 + self.cell_size_y

        self._cells[i][j].draw(current_cell_x1, current_cell_y1, current_cell_x2, current_cell_y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
