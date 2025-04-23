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
            top = [i, j-1]
            bottom = [i, j+1]
            left = [i-1, j]
            right = [i+1, j]

            dir_choice = [top, bottom, left, right]
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

            if new_direction == top:
                self._cells[i][j].has_top_wall = False
                self._cells[new_x][new_y].has_bottom_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            elif new_direction == bottom:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_x][new_y].has_top_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            elif new_direction == left:
                self._cells[i][j].has_left_wall = False
                self._cells[new_x][new_y].has_right_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            elif new_direction == right:
                self._cells[i][j].has_right_wall = False
                self._cells[new_x][new_y].has_left_wall = False
                self._draw_cell(i,j)
                self._draw_cell(new_x,new_y)
            

            self._break_walls_r(new_x,new_y)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False


    def solve(self):
        solved = self._solve_r(0,0)
        return solved
    
    def _solve_r(self, i, j):
        self._animate()
        #Marking current cell as visited
        self._cells[i][j].visited = True

        #Bottom right = exit; if current cell is bot right, return
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        to_visit = []

        #Top Check = i, j-1
        #Can't move north to move out of bounds south, so just checking if j is larger than 0
        #Since both cells already have walls broken, only have to check one cell wall
        #Don't need to visit again if already visited
        if j - 1 >= 0 and self._cells[i][j].has_top_wall is False and self._cells[i][j-1].visited is False:
            to_visit.append([i,j-1])

        #Bottom Check = i, j+1
        #Similar to top check, but checking if j will be less than num_rows
        if j + 1 < self.num_rows and self._cells[i][j].has_bottom_wall is False and self._cells[i][j+1].visited is False:
            to_visit.append([i,j+1])

        #Left Check = i-1, j
        #Similar to top check, but checking if i will be larger than 0
        if i - 1 >= 0 and self._cells[i][j].has_left_wall is False and self._cells[i-1][j].visited is False:
            to_visit.append([i-1,j])

        #Right Check = i+1, j
        #Similar to top check, but checking if i will be less than num_cols
        if i + 1 < self.num_cols and self._cells[i][j].has_right_wall is False and self._cells[i+1][j].visited is False:
            to_visit.append([i+1,j])

        for dir in to_visit:
            new_i = dir[0]
            new_j = dir[1]
            self._cells[i][j].draw_move(self._cells[new_i][new_j])
            result = self._solve_r(new_i, new_j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[new_i][new_j],True)
        return False