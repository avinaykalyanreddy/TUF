"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


"""
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]



n = len(triangle)-1
seen = {}
def recursion(row,col):

    if row == n:

        return triangle[row][col]

    if (row,col) in seen:

        return  seen[(row,col)]

    left = recursion(row+1,col)
    right = recursion(row+1,col+1)

    seen[(row,col)] = triangle[row][col] + min(left,right)

    return  seen[(row,col)]

print(recursion(0,0))