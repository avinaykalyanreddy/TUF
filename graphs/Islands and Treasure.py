"""
You are given a
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""
from collections import deque
# logic first fill all 1's in respectivw grid usigng bfs
grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]


visited = set()
q = deque()


n = len(grid)
m  = len(grid[0])

for i in range(n):

    for j in range(m):

        if grid[i][j] == 0:

            q.append((i,j))
            visited.add((i,j))

def bfs(row,col):

    if row < 0 or row == n or col < 0 or col == m or (row,col)  in visited or grid[row][col] == -1:

        return

    q.append((row,col))
    visited.add((row,col))

dist = 0
while q:

    for i in range(len(q)):

        r,c = q.popleft()

        grid[r][c] = dist

        bfs(r,c-1)
        bfs(r,c+1)

        bfs(r-1,c)
        bfs(r+1,c)



    dist += 1

print(grid)