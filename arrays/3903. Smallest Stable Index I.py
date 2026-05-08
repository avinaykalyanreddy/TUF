"""
You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

max(nums[0..i]) is the largest value among the elements from index 0 to index i.
min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.


"""

nums = [6,1,4]; k = 5


l = len(nums)

c = [None]*l
p = [None]*l

m = float("-inf")

for idx,val in enumerate(nums):

    m = max(m,val)

    p[idx] = m

m = float("inf")

for i in range(l-1,-1,-1):

     m = min(m,nums[i])
     c[i] = m
print(p,c)
res = -1
mi = float("inf")

for i in range(l):

    val = p[i] - c[i]

    if val  <= k:

        if val < mi:
            mi = val
            res = i

print(res)
