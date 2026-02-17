"""
You are given an integer array nums of size n, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Note: [1,0,3,2] and [3,0,1,2] are considered as same quadruplets.


"""

nums=[2,2,2,2,2];target = 8



nums.sort()

res = []
n = len(nums)
for i in range(n-3):

    if i > 0 and nums[i] == nums[i-1]:

        continue

    for j in range(i+1,n-2):

        if j > i+1 and nums[j] == nums[j-1]:
            continue

        low = j+1
        high = n-1

        while low < high:

            total = nums[i]+nums[j] + nums[low] + nums[high]

            if total == target:

                res.append([nums[i],nums[j],nums[low],nums[high]])

                while low < high and nums[low] == nums[low + 1]:
                    low += 1

                while low < high and nums[high] == nums[high-1]:

                    high -= 1

                low += 1
                high -= 1

            elif total > target:

                high -= 1
            else:

                low += 1
print(res)