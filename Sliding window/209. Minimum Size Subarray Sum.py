"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

target = 11; nums = [1,1,1,1,1,1,1,1]



left = 0
res = float("inf")
sum = 0

for right in range(len(nums)):

    sum = sum + nums[right]

    while sum >= target:

        sum = sum - nums[left]

        res = min(res,right - left + 1)

        left += 1

print(res)