"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

nums = [0,3,2,5,4,6,1,1]



s = set(nums)

res = 0

for i in nums:

    if i  - 1 not in s:

        l = 0


        while i+l in s:

            l += 1

        res = max(res,l)

print(res)