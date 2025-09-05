"""
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].


"""

nums = [1,2,3,4,3,2,5]; k = 3


if k == 1:

    print(nums)
    exit()

n = len(nums)
res = [-1] * (n - k + 1)

left = 0

for right in range(n):

    if nums[right] - nums[right-1] != 1:

        left = right

    if right - left + 1 > k:

        left = left + 1

    if right - left + 1 == k:

        res[left] = nums[right]

print(res)