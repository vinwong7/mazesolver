from window import Window, Line, Point

def main():
    win = Window(800, 600)
    
    pt1 = Point(100,200)
    pt2 = Point(100,400)
    line1 = Line(pt1, pt2)
    win.draw_line(line1,"black") 
    
    pt3 = Point(0,0)
    pt4 = Point(800,600)
    line2 = Line(pt3, pt4)
    win.draw_line(line2,"green") 
    
    win.wait_for_close()


main()