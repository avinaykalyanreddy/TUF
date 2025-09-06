"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
from collections import deque

nums = [1,3,-1,-3,5,3,6,7]; k = 3

res = []

left = 0

max_val = deque()


for right in range(len(nums)):

    while max_val and max_val[-1] < nums[right]:

        max_val.pop()

    max_val.append(nums[right])

    while right - left + 1 > k:

        if nums[left] == max_val[0]:

            max_val.popleft()

        left += 1

    if right - left + 1 == k:

        res.append(max_val[0])

print(res)