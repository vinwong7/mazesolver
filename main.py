from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(25,25,10,10,25,25,win)


    win.wait_for_close()


main()