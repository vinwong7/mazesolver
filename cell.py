from graphics import Line, Point

class Cell:
    def __init__(self, windows):
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
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_left_wall is True:
            pt1 = Point(self.x1, self.y1)
            pt2 = Point(self.x1, self.y2)
            line = Line(pt1, pt2)
            line.draw(self.win.canvas)

        if self.has_right_wall is True:
            pt1 = Point(self.x2, self.y1)
            pt2 = Point(self.x2, self.y2)
            line = Line(pt1, pt2)
            line.draw(self.win.canvas)

        if self.has_top_wall is True:
            pt1 = Point(self.x1, self.y1)
            pt2 = Point(self.x2, self.y1)
            line = Line(pt1, pt2)
            line.draw(self.win.canvas)

        if self.has_bottom_wall is True:
            pt1 = Point(self.x1, self.y2)
            pt2 = Point(self.x2, self.y2)
            line = Line(pt1, pt2)
            line.draw(self.win.canvas)
        
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

