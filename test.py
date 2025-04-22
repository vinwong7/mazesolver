import unittest
from maze import Maze

class Tests_Maze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 30
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_exit(self):
        num_cols = 30
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False,
        )

    def test_maze_break_entrance_exit_2(self):
        num_cols = 5
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False,
        )

    def test_maze_visited_reset(self):
        num_cols = 5
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        comparison = []
        for i in range(num_cols*num_rows):
            comparison.append(False)
        m1_comparison = []
        for a in range(num_cols):
            for b in range(num_rows):
                m1_comparison.append(m1._cells[a][b].visited)
        self.assertEqual(
            m1._cells[0][0].visited,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].visited,
            False,
        )
        self.assertEqual(
            m1_comparison,
            comparison,
        )

if __name__ == "__main__":
    unittest.main()

