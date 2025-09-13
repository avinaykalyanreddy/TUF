"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.


"""

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

n = len(grid1)
m = len(grid1[0])


def dfs(row,col):


    if row < 0 or row == n or col < 0 or col == m or grid2[row][col] == 0:

        return True

    if grid2[row][col] != grid1[row][col]:

        return False

    grid2[row][col] = 0
    return dfs(row,col-1) and dfs(row,col+1) and dfs(row-1,col) and dfs(row+1,col)


res = 0
for i in range(n):

    for j in range(m):


        if grid2[i][j] != 0 and dfs(i,j):

            res += 1

print(res)