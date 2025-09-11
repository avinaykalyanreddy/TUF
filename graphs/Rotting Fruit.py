from collections import deque


grid = grid = [[1,0,1],[0,2,0],[1,0,1]]



q = deque()
visited = set()

n = len(grid)
m = len(grid[0])
fresh = 0
res = 0
for i in range(n):
    for j in range(m):

        if grid[i][j] == 2:

            q.append((i, j))

            visited.add((i, j))

        elif grid[i][j] == 1:

            fresh += 1

if fresh == 0: # if there is no fresh fruits rotten time takes 0
    print(0)
    exit()




def bfs(r, c):
    global  fresh
    if r < 0 or r == n or c < 0 or c == m or (r, c) in visited or grid[r][c] == 0:
        return

    visited.add((r, c))
    q.append((r, c))
    fresh -= 1



while q:

    for _ in range(len(q)):
        row, col = q.popleft()

        bfs(row, col - 1)

        bfs(row, col + 1)

        bfs(row + 1, col)

        bfs(row - 1, col)

    res += 1

print(res-1) if fresh == 0 else print(-1)
