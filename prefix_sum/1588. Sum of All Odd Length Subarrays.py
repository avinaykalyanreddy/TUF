"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
"""

arr = [1,4,2,5,3]

res = 0
n = len(arr)

for i in range(n):

    left = i + 1
    right = n-i

    total_sub = left * right

    odd_sub = total_sub//2 + total_sub % 2

    res += arr[i] * odd_sub

print(res)