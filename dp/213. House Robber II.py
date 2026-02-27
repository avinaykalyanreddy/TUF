"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

#there two conditons strat from 0 index and end it n-2 because 0 and n-1 are adjacent we go in forward direction only
# strat from 1 and ent it n-1 because 1 and 0 are adjacent we go in forward direction only

class Solution:
    def rob(self, nums) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        dic = {}

        def robber(idx, n):

            if idx >= n:
                return 0

            if idx not in dic:
                dic[idx] = max(nums[idx] + robber(idx + 2, n), robber(idx + 1, n))

            return dic[idx]

        x = robber(0, n - 1)
        dic = {}
        y = robber(1, n)

        return max(x, y)
