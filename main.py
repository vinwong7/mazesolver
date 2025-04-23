from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(25,25,12,16,25,25,win)

    if maze.solve():
        print("Maze solved.")
    else:
        print("Unsolvable maze.")

    win.wait_for_close()


main()