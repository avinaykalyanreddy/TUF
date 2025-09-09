"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
import collections

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

n = len(grid)
m = len(grid[0])


res = 0
"""
def max_area(i,j):

    if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:

        grid[i][j] = 0

        return 1 + max_area(i+1,j) + max_area(i-1,j) + max_area(i,j+1) + max_area(i,j-1)

    return 0


for i in range(n):

    for j in range(m):

        if grid[i][j] == 1:


            res = max(max_area(i,j),res)
"""

n = len(grid)
m = len(grid[0])

res = 0

visited = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(i, j):
    q = collections.deque()

    q.append((i, j))
    visited.add((i, j))
    area = 1
    while q:

        row, col = q.popleft()

        for dr, dc in directions:

            r, c = row + dr, col + dc

            if 0 <= r < n and 0 <= c < m and (r, c) not in visited and grid[r][c] == 1:
                area += 1

                q.append((r, c))
                visited.add((r, c))

    return area


for i in range(n):

    for j in range(m):

        if grid[i][j] == 1:
            res = max(bfs(i, j), res)

print(res)