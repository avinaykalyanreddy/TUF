"""
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.


"""

nums = [1,2,3,1,2,3,1,2]; k = 2


dic = {}
res = 0

left = 0

for right in range(len(nums)):

    dic[nums[right]] = 1 + dic.get(nums[right],0)

    while left <= right and dic[nums[right]] > k:

        dic[nums[left]] -= 1

        left += 1

    res = max(res,right - left +1 )

print(res)