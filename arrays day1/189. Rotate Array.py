"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
nums = [1,2,3,4,5,6,7];k = 3

n = len(nums)
start = k % n


# Solution 1
""""
lst = []


for i in range(start,0,-1):

    lst.append(nums[-i])

for i in range(0,n-start):

    lst.append(nums[i])

for i in range(n):

    nums[i] = lst[i]

print(nums)

"""

def reverse(low,high):

    while low < high:

        nums[low],nums[high] = nums[high],nums[low]

        low += 1
        high -= 1


reverse(n-start,n-1)
reverse(0,n-start-1)
reverse(0,n-1)
print(nums)