"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

"""
class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        seen = {}

        def recursion(s):

            if s in seen:

                return seen[s]
            if s == target:

                return 1

            if s > target:

                return 0

            ans = 0

            for i in nums:

                ans += recursion(s+i)
            seen[s] = ans
            return seen[s]
        return(recursion(0))