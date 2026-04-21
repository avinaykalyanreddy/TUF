"""
You are given an integer array nums consisting only of 0, 1, and 2.

A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.

Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1.

The absolute difference between indices i and j is defined as abs(i - j).
"""
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        check = True

        res = float("inf")

        idx = -1

        for i,j in enumerate(nums):

            if j == 0:
                continue

            if check is True:

                idx = i

                check = j

            elif check != j:

                res = min(res,i-idx)
                idx = i
                check = j

            elif check == j:

                idx = i
        return res if res != float("inf") else -1

