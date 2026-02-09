"""
You are given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


"""

"""
nums = [1,2,4,5,6,3,1]

n = len(nums)

i = 0

while i < n:

    if nums[i] <= 0 or nums[i] > n:

        i += 1

        continue

    idx = nums[i] - 1

    if nums[i] != nums[idx]:

        nums[i],nums[idx] = nums[idx],nums[i]

    else:

        i += 1

for i in range(n):

    if i+1 != nums[i]:

        print(i+1)
        exit()

print(n+1)
"""

nums = [1,2,4,5,6,3,7]

n = len(nums)

for i in range(n):

    if nums[i] < 0:

        nums[i] = 0

for i in range(n):

    val = abs(nums[i])

    if 1 <= val <= n:

        if nums[val - 1] > 0:

            nums[val - 1] *= -1

        elif nums[val - 1] == 0:

            nums[val - 1] = -(n+1)

for i in range(n):

    if nums[i] >= 0:

        print(i+1)
        exit()

print(n+1)