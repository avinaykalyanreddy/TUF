"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""

mat = [[0,0],[0,0],[1,0]]

row = {}

n = len(mat)
m = len(mat[0])

for i in range(n):

    cnt = 0

    for j in range(m):

        if mat[i][j] == 0:

            cnt += 1

    row[i] = cnt

col = {}

for i in range(m):
    cnt = 0
    for j in range(n):

        if mat[j][i] == 0:

            cnt += 1

    col[i] = cnt
res = 0
for i in range(n):

    for j in range(m):

        if mat[i][j] == 1:

            if row[i] == m-1 and col[j] == n-1:
                res = res+1
print(row,col)
print(res)
