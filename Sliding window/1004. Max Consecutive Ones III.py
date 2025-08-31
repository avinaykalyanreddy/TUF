"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

# if in the question they ask consecutive go with a sliding window

nums = [1,1,1,0,0,0,1,1,1,1,0];k = 2


res = 0
left = 0

cnt_zero = 0

for right in range(len(nums)):

    if nums[right] == 0:

        cnt_zero += 1


    while cnt_zero > k:

        if nums[left] == 0:

            cnt_zero -= 1

        left += 1

    res = max(res,right-left+1)

print(res)

