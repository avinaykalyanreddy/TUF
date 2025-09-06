"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
"""

from collections import deque

nums = [2,2,2,4,4,2,5,5,5,5,5,2]; limit = 2



max_q = deque()
min_q = deque()

left  = 0

res = 0

for right in range(len(nums)):

    while max_q and nums[right] > max_q[-1]:

        max_q.pop()
    while min_q and nums[right] < min_q[-1]:

        min_q.pop()
    max_q.append(nums[right])
    min_q.append(nums[right])

    while  max_q[0] - min_q[0] > limit:

        if max_q[0] == nums[left]:

            max_q.popleft()

        if min_q[0] == nums[left]:

            min_q.popleft()

        left += 1

    res = max(res,right - left + 1)


print(res)