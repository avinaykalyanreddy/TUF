"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.


"""

board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

print(board)
n = len(board)
m = len(board[0])


def dfs(row,col):

    if row < 0 or col < 0 or row == n or col == m or board[row][col] == "X" or board[row][col] == "-1":

        return

    board[row][col] = "-1"

    dfs(row,col-1)
    dfs(row,col+1)
    dfs(row-1,col)
    dfs(row+1,col)


for col in range(m):

    if board[0][col] == "O":

        dfs(0,col)

    if board[n-1][col] == "O":

        dfs(n-1,col)

for row in range(n):

    if board[row][0] == "O":

        dfs(row,0)

    if board[row][m-1] == "O":

        dfs(row,m-1)

for i in range(n):

    for j in range(m):


        if board[i][j] == "-1":

            board[i][j] = "O"

        elif board[i][j] == "O":

            board[i][j] = "X"

print(board)