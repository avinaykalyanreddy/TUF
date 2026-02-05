"""
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.
nums = [1,3,5,4,2,6]


"""


class Solution:
    def isTrionic(self, nums):

        n = len(nums)

        if n == 3:
            return False
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        if i == 0:
            return False

        j = i

        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1

        if j == i:
            return False

        k = j

        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1

        if k == j:
            return False
        return k == n - 1