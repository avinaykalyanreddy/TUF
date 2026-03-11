"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""
matrix = [[2,1,3],[6,5,4],[7,8,9]]

n = len(matrix)
m = len(matrix[0])
res = float("inf")

seen = {}
def recursion(row,col):

    if (row,col) in seen:
        return seen[(row,col)]
    if  col < 0 or col > m-1:

        return float("inf")

    if row == n-1:

        return matrix[row][col]

    ans = float("inf")

    ans = min(ans,matrix[row][col]+recursion(row+1,col-1))
    ans = min(ans,matrix[row][col]+recursion(row+1,col))
    ans = min(ans,matrix[row][col]+recursion(row+1,col+1))
    seen[(row,col)] = ans
    return seen[(row,col)]
for i in range(m):

    res = min(recursion(0,i),res)

print(res)