PATH = "_"
START = 'S'
VISITED = "."
# using ord required me to start it at the char before a
SOLUTION = ord('`')


def get_solution_char():
    global SOLUTION
    if SOLUTION >= ord('z'):
        SOLUTION = ord('a')
    else:
        SOLUTION += 1
    return chr(SOLUTION)


class Maze:

    def __init__(self, ascii_maze):
        # splits maze string into separate values on each new line
        # uses list comp. to create 'matrix' out of maze
        self.maze = [list(row) for row in ascii_maze.splitlines()]
        # finds index first '_' character which denotes the beginning
        self.start_y = [row.count(START) for row in self.maze].index(1)
        # finds position where '_' is located within the 'y' line which returns the index position
        self.start_x = self.maze[self.start_y].index(START)

    # returns string representation of maze object, joining maze elements passed in as parameters
    # used to print maze with 'cells' and be user friendly
    def __repr__(self):
        return "\n".join("".join(row) for row in self.maze)

    def solve_maze(self, x=None, y=None):
        # assigns starting (x,y) position
        if x is None:
            x, y = self.start_x, self.start_y
        # checks if the coordinate is in the path/start
        if self.maze[y][x] in (PATH, START):
            # marks spot as 'visited' for recursion check
            self.maze[y][x] = VISITED
            # uses recursion to check paths by checking each direction and making a decision off that
            try:
                if (self.solve_maze(x + 1, y) or
                        self.solve_maze(x - 1, y) or
                        self.solve_maze(x, y - 1) or
                        self.solve_maze(x, y + 1)):
                    self.maze[y][x] = get_solution_char()
                    return True
            # this exception is what occurs when the program tries to leave the maze (aka it found the exit)
            # also marks it
            except IndexError:
                self.maze[y][x] = get_solution_char()
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
        # converting to string allows for easy replacement of things
        maze = str(maze)
        maze = maze.replace(".", "_")
    print(maze)

