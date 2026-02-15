"""
You are given an integer array nums.

Return an integer denoting the first element (scanning from left to right) in nums whose frequency is unique. That is, no other integer appears the same number of times in nums. If there is no such element, return -1.
"""


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        s = {}

        for i, j in dic.items():

            if j not in s:

                s[j] = [1, i]

            else:

                s[j][0] += 1

        for i in s:

            if s[i][0] == 1:
                return (s[i][1])

        return -1