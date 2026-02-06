"""
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.

"""
class Solution:
    def matrixBlockSum(self, mat, k):
        row = len(mat)+1
        col = len(mat[0] ) + 1

        new_mat = [[0]*col for _ in range(row)]


        for i in range(1,row):

            for j in range(1,col):

                new_mat[i][j] = new_mat[i][j-1] + new_mat[i-1][j] - new_mat[i-1][j-1] + mat[i-1][j-1]

        res  = []

        for i in range(1,row):
            x = []
            for j in range(1,col):

                row1 = i - k if i - k > 0 else 1

                row2 = i + k if i + k < row else row - 1

                col1 = j - k if j - k > 0 else 1

                col2 = j + k if j + k < col else col - 1


                s = new_mat[row2][col2] - new_mat[row1-1][col2] - new_mat[row2][col1-1] + new_mat[row1-1][col1-1]

                x.append(s)

            res.append(x)

        return (res)
