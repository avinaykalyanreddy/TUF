"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
"""

import collections

grid = [[6,1,10]]

n = len(grid)
m = len(grid[0])

res = 0

visited = set()
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(i,j):
    fishes = 0
    q = collections.deque()

    visited.add((i,j))
    q.append((i,j))

    fishes += grid[i][j]

    while q:

        row,col = q.popleft()

        for dr,dc in directions:

            r,c = row + dr, col + dc

            if 0 <= r < n and 0 <= c < m and (r,c) not in visited and grid[r][c] > 0:

                fishes += grid[r][c]

                visited.add((r,c))

    return fishes




for i in range(n):

    for j in range(m):

        if grid[i][j] > 0:

            res = max(res,bfs(i,j))


print(res)