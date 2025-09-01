"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
"""

nums = [9,4,1,7]; k = 2


nums.sort()

left = 0
res = float("inf")
n = len(nums)

for right in range(n):

    if right - left + 1 == k:

        res = min(res,nums[right] - nums[left])

        left += 1


print(res)
