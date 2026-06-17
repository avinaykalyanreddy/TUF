"""
You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

max(nums[0..i]) is the largest value among the elements from index 0 to index i.
min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.
"""
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        maxi = []
        mini = []

        m = float("-inf")
        for i in nums:
            m = max(m, i)
            maxi.append(m)
        m = float('inf')
        for i in range(l - 1, -1, -1):
            m = min(m, nums[i])

            mini.append(m)

        mini.reverse()

        for i in range(l):

            if maxi[i] - mini[i] <= k:
                return (i)

        return -1