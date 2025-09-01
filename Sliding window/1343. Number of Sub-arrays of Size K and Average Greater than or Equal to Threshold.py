"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
"""

arr = [2,2,2,2,5,5,5,8]; k = 3; threshold = 4

res = 0

partial_sum = 0

n = len(arr)

left = 0

for right in range(n):

    partial_sum += arr[right]

    if right - left + 1 == k:

        if partial_sum/k >= threshold:

            res += 1

        partial_sum -= arr[left]
        left += 1


print(res)

