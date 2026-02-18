"""
You are given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

nums = [-4,-1,0,3,10]
low = 0
high  = len(nums)-1


res = []

while low <= high:

    if  abs(nums[high]) >= abs(nums[low]) :

        val = nums[high]

        high -= 1

    else:

        val = nums[low]

        low += 1

    res.append(val**2)

print(res[::-1])