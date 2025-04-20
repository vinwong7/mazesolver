from graphics import Line, Point

class Cell:
    def __init__(self, windows=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.win = windows
    
    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        
        left_pt1 = Point(self.x1, self.y1)
        left_pt2 = Point(self.x1, self.y2)
        left_line = Line(left_pt1, left_pt2)
        if self.has_left_wall:
            left_line.draw(self.win.canvas)
        else:
            left_line.draw(self.win.canvas, "white")

        right_pt1 = Point(self.x2, self.y1)
        right_pt2 = Point(self.x2, self.y2)
        right_line = Line(right_pt1, right_pt2)
        if self.has_right_wall is True:
            right_line.draw(self.win.canvas)
        else:
            right_line.draw(self.win.canvas, "white")


        top_pt1 = Point(self.x1, self.y1)
        top_pt2 = Point(self.x2, self.y1)
        top_line = Line(top_pt1, top_pt2)
        if self.has_top_wall:
            top_line.draw(self.win.canvas)
        else:
            top_line.draw(self.win.canvas, "white")

        bottom_pt1 = Point(self.x1, self.y2)
        bottom_pt2 = Point(self.x2, self.y2)
        bottom_line = Line(bottom_pt1, bottom_pt2)
        if self.has_bottom_wall:
            bottom_line.draw(self.win.canvas)
        else:
            bottom_line.draw(self.win.canvas, "white")

    def draw_move(self, to_cell, undo=False):
        center1_x = (self.x1 + self.x2)//2
        center1_y = (self.y1 + self.y2)//2

        center2_x = (to_cell.x1 + to_cell.x2)//2
        center2_y = (to_cell.y1 + to_cell.y2)//2

        center1 = Point(center1_x, center1_y)
        center2 = Point(center2_x, center2_y)

        center_line = Line(center1, center2)

        if undo is False:
            self.win.draw_line(center_line, "red")
        else:
            self.win.draw_line(center_line, "gray")

