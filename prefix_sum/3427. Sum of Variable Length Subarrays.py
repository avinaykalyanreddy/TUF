
"""
You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array.
"""

nums = [2,3,1]
""" This is my answer
prefix_sum = [nums[0]]
n = len(nums)
for i in range(1,n):

    prefix_sum.append(prefix_sum[-1]+nums[i])

res = 0
for i in range(n):

     start = max(0,i-nums[i])

     if start == 0:

         res += prefix_sum[i]

     else:

         res += prefix_sum[i] - prefix_sum[start-1]

print(res)
"""

# optimal solution

res = 0
prefix_sum = 0
prefix_arr = [0]
n = len(nums)

for i in range(n):

    prefix_sum += nums[i]

    prefix_arr.append(prefix_sum)

    start = max(0,i-nums[i])

    res += prefix_sum - prefix_arr[start]

print(res)