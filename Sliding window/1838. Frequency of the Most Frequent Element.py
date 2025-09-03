"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

"""

nums = [2,3,4,4,4,6,7]
k = 5

nums.sort()
left = 0
total = 0
res = 0

for right in range(len(nums)):

    total += nums[right]

    while nums[right] * (right - left + 1) - total > k : # formula to get number times k is used if used in > k then run the loop

        total  -= nums[left]

        left += 1

    res = max(res,right-left + 1)

print(res)