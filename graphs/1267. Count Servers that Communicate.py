"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
"""

# tip search for isolated server and minus for total server
# use row and column wise search

grid = [[1,0],[0,1]]

isolated_servers = 0
total_servers = 0

n = len(grid)
m = len(grid[0])
def row(r,c):

    for row in range(n):

        if (r,c) != (row,c) and grid[row][c] == 1:

            return  False


    return True


def col(r,c):

    for col in range(m):

        if (r,c) != (r,col) and grid[r][col] ==1 :

            return  False


    return  True


for i in range(n):

    for j in range(m):

        if grid[i][j] == 1:

            total_servers += 1

            if row(i,j) and col(i,j):

                isolated_servers += 1

print(total_servers - isolated_servers)
