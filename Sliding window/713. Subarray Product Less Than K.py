"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
"""
nums = [10,5,2,6]; k = 100

left = 0
cur  = 1

res = 0

for right in range(len(nums)):

    cur = cur * nums[right]

    while left <= right and  cur >= k:

        cur = cur / nums[left]

        left += 1

    res = res + (right - left + 1)

print(res)