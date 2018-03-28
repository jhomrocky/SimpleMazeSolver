
ASCII_MAZE = """
###S###
#_____#
#_##_##
#_##__#
#_##__#
#E#####
"""

PATH = "_"
START = "_"
EXIT = "E"
VISITED = "."
SOLUTION = "o"


class Maze:
    def __init__(self, ascii_maze):
        # splits maze string into separate values on each new line
        # uses list comp. to create 'matrix' out of maze
        self.maze = [list(row) for row in ascii_maze.splitlines()]
        # finds index of starting cells by iterating through to find 'S'
        # puts into list, finds the index (position/coordinate) set to '1' since all others are 0 (false)
        self.start_y = [row.count(START) for row in self.maze].index(1)
        # finds position where 'S' is located within the 'y' line which returns the index position
        self.start_x = self.maze[self.start_y].index(START)

    # returns string representation of maze object, joining maze elements passed in as parameters
    # used to print maze with 'cells'
    def __repr__(self):
        return "\n".join("".join(row) for row in self.maze)

    def solve_maze(self, x=None, y=None):
        if x is None:
            x, y = self.start_x, self.start_y
        if self.maze[y][x] in (PATH, START):
            self.maze[y][x] = VISITED
            if (self.solve_maze(x+1, y) or
                    self.solve_maze(x-1, y) or
                    self.solve_maze(x, y+1) or
                    self.solve_maze(x, y-1)):
                self.maze[y][x] = SOLUTION
                return True
        elif self.maze[y][x] == EXIT:
            self.maze[y][x] = SOLUTION
            return True
        return False


if __name__ == "__main__":
    import sys
    # for checking mazes through terminal
    if len(sys.argv) > 1:
        maze = Maze(open(sys.argv[1]).read())
    # if none available, defaults to 'maze' text file
    else:
        maze = Maze(open('maze').read())
    # prints string representation of maze to replace "visited" areas (. char used for testing) with original "_"
    if maze.solve_maze():
        print(str(maze).replace(".", "_"))