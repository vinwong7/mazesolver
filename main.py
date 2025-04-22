from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(25,25,20,20,25,25,win,0)
    maze._break_entrance_and_exit()

    maze._break_walls_r(0,0)

    win.wait_for_close()


main()