"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

nums = [1,2,2,3,3,3], k = 2

"""
import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        dic  = collections.defaultdict(int)

        for i in nums:

            dic[i] += 1

        buckets = [[] for i in range(len(nums)+1)]

        for num,freq in dic.items():

            buckets[freq].append(num)
        res = []
        for i in range(len(nums),-1,-1):

            for j in buckets[i]:

                if k == 0:
                    break

                res.append(j)
                k = k - 1

        return res


