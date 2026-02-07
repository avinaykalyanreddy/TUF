"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O
(
n
)
O(n) time without using the division operation?
"""

nums = [1,2,4,6]

res = []
prod = 1

for i in nums:

    prod *= i

    res.append(prod)


prod = 1

for i in range(len(nums)-1,0,-1):

    res[i] = res[i-1] * prod

    prod *= nums[i]


res[0] = prod

print(res)