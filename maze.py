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
        
        self._cells = []
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
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            cell_column = []
            for j in range(self.num_rows):
                cell_column.append(Cell(self.win))
            self._cells.append(cell_column)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True    

        while True:
            north = [i, j-1]
            south = [i, j+1]
            west = [i-1, j]
            east = [i+1, j]

            dir_choice = [north, south, west, east]
            to_visit = []

            for dir in dir_choice:
                x = dir[0]
                y = dir[1]

                if x < 0 or y < 0:
                    continue
                elif x >= self.num_cols or y >= self.num_rows:
                    continue
                elif self._cells[x][y].visited:
                    continue
                else:
                    to_visit.append(dir)

            if len(to_visit) == 0:
                return
            
            ran_num = random.randrange(0, len(to_visit), 1)
            new_direction = to_visit[ran_num]
            new_x = new_direction[0]
            new_y = new_direction[1]

            if new_direction == north:
                self._cells[i][j].has_top_wall = False
                self._cells[new_x][new_y].has_bottom_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            elif new_direction == south:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_x][new_y].has_top_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            elif new_direction == west:
                self._cells[i][j].has_left_wall = False
                self._cells[new_x][new_y].has_right_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            elif new_direction == east:
                self._cells[i][j].has_right_wall = False
                self._cells[new_x][new_y].has_left_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            

            self._break_walls_r(new_x,new_y)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False