class Solution:
    def findDiagonalOrder(self, mat) :

        n = len(mat)
        m = len(mat[0])

        row = 0
        col = 0
        res = []
        for _ in range(n * m):

            res.append(mat[row][col])

            if (row + col) % 2 == 0:

                if col == m - 1:

                    row = row + 1

                elif row == 0:

                    col += 1


                else:

                    row = row - 1
                    col += 1

            else:

                if row == n - 1:

                    col = col + 1

                elif col == 0:

                    row = row + 1

                else:

                    row = row + 1

                    col = col - 1

        return (res)

