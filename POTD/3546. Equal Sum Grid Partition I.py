"""
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.


"""
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sum = []
        col_sum = []

        total = 0
        for i in grid:
            x = sum(i)
            row_sum.append(x)

            total += x

        n = len(grid)
        m = len(grid[0])

        for i in range(m):
            x = 0
            for j in range(n):

               x = x + grid[j][i]


            col_sum.append(x)

        def checking(lst):

            pre_sum = 0

            for i in lst:

                pre_sum += i

                if total-pre_sum == pre_sum:

                    return True

            return False

        return checking(row_sum) or checking(col_sum)