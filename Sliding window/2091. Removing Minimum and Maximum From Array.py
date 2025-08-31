"""
You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array

"""

# there are only 3 scenario only

nums = [2,10,7,5,4,1,8,6]


min_idx = nums.index(min(nums))

max_idx = nums.index(max(nums))

n = len(nums)

left = max(min_idx,max_idx)+1

right = max(n-min_idx,n-max_idx)


both = min(min_idx,max_idx)+1 + min(n-min_idx,n-max_idx)


print(min(left,right,both))