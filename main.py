from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    Maze(25,25,20,4,10,10,win)

    win.wait_for_close()


main()