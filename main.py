from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(25,25,5,5,40,40,win,0)
    maze._break_entrance_and_exit()
    win.wait_for_close()


main()