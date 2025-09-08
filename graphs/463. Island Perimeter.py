"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]


n = len(grid)
m = len(grid[0])

def perimeter(i,j):

    if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:

        grid[i][j] = 2

        return 0 + perimeter(i,j-1) + perimeter(i,j+1) + perimeter(i-1,j) + perimeter(i+1,j)

    elif 0 <= i < n and 0 <= j < m and grid[i][j] == 2:

        return 0

    return 1

for i in range(n):

    for j in range(m):

        if grid[i][j] == 1:

            print(perimeter(i,j))
            break