
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

nums = [1,1,0,1,1,1]

res = cnt = 0

for i in nums:

    if i == 1:

        cnt += 1

    else:

        cnt = 0

    res = max(res,cnt)

print(res)