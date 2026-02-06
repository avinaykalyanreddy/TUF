"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""


class NumMatrix: # explanation from techdose

    def __init__(self, matrix):

        row = len(matrix) + 1
        col = len(matrix[0]) + 1

        self.new_mat = [[0] * col for _ in range(row)]

        for i in range(1, row):

            for j in range(1, col):
                self.new_mat[i][j] = self.new_mat[i][j - 1] + self.new_mat[i - 1][j] - self.new_mat[i - 1][j - 1] + \
                                     matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1 = row1 + 1
        col1 = col1 + 1

        row2 = row2 + 1

        col2 = col2 + 1

        return self.new_mat[row2][col2] - self.new_mat[row1 - 1][col2] - self.new_mat[row2][col1 - 1] + \
            self.new_mat[row1 - 1][col1 - 1]

"""
# my solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.mat1 = matrix
        self.mat2 = []

        x = 0

        for i in range(len(matrix)):
            y = []
            for j in range(len(matrix[0])):

                x = x + matrix[i][j]
                y.append(x)

            self.mat2.append(y)


                


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
            res = 0
            for i in range(row2-row1+1):

                sub = self.mat2[row1+i][col2] - self.mat2[row1+i][col1]

                res += sub + self.mat1[row1+i][col1]

            return res
"""