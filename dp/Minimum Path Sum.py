"""
Ninjaland is a country in the shape of a 2-Dimensional grid 'GRID', with 'N' rows and 'M' columns. Each point in the grid has some cost associated with it.



Find a path from top left i.e. (0, 0) to the bottom right i.e. ('N' - 1, 'M' - 1) which minimizes the sum of the cost of all the numbers along the path. You need to tell the minimum sum of that path.



Note:
You can only move down or right at any point in time.
"""

grid = [[1,2,3],[4,5,4],[7,5,9]]

n = len(grid)-1
m = len(grid[0])-1
seen = {}
def recursion(row,col):

    if row == n and col == m:

        return grid[row][col]


    if (row,col)  in seen:

        return seen[(row,col)]

    right = float("inf")
    down = float("inf")
    if col + 1 <= m:

        right = recursion(row,col+1)

    if row + 1 <= n :

        down = recursion(row+1,col)

    seen[(row,col)] = grid[row][col] + min(right,down)
    return seen[(row,col)]


print(recursion(0,0))
