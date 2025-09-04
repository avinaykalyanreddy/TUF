"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

means Remove either the first element (leftmost) or the last element (rightmost) of the array
"""

nums = [1,1,4,2,3]; x = 5 # find the subarray sum(nums) - k because Remove either the first element (leftmost) or the last element (rightmost) of the array

s = sum(nums)-x

left = 0
res = float("inf")

total = 0
n = len(nums)
for right in range(n):

    total += nums[right]

    while left <= right and total >  s:

        total -= nums[left]

        left += 1

    if total == s:

        res = min(res,n-(right - left +1))


print(res)