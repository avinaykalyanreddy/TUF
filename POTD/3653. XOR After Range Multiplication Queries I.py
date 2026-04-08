"""
You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].

For each query, you must apply the following operations in order:

Set idx = li.
While idx <= ri:
Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
Set idx += ki.
Return the bitwise XOR of all elements in nums after processing all queries.
"""
nums = [2,3,1,5,4];queries = [[1,4,2,3],[0,2,1,2]]



for i in queries:

    l,r,k,v = i

    idx = l

    while idx <= r:

        nums[idx] = (nums[idx]*v)%(10**9+7)

        idx += k

res = nums[0]

for i in range(1,len(nums)):

    res = res ^ nums[i]


print(res)