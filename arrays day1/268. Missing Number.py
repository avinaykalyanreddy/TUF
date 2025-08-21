"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
read problem statement correctly

"""

nums = [3,0,1]


n = len(nums)

total = (n*(n+1))//2

for i in nums:

    total -= i

print(total)