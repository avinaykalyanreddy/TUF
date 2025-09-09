import collections

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

n = len(grid)
m = len(grid[0])

res = 0
# using dfs
"""
def finding_island(i,j):

    if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":


        grid[i][j] = "0"

        finding_island(i+1,j)
        finding_island(i-1,j)

        finding_island(i,j+1)
        finding_island(i,j-1)




for i in range(n):

    for j in range(m):

        if grid[i][j] == "1":

            finding_island(i,j)

            res += 1

print(res)

"""
# using BFS


visited = set()

def bfs(i,j):

    q = collections.deque()

    q.append((i,j))

    visited.add((i,j))

    while q:

        row,col = q.popleft()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in directions:

            r,c = row+dr,col+dc

            if 0 <= r < n and 0 <= c < m and (r,c) not in visited and grid[r][c] == "1" :

                q.append((r,c))

                visited.add((r,c))


for i in range(n):

    for j in range(m):

        if grid[i][j] == "1"  and (i,j) not in visited:

            res += 1

            bfs(i,j)
print(res)