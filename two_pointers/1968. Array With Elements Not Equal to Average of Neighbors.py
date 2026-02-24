nums = [1, 2, 5, 9]

"""
conditions 
left should be smaller than mid
right should be smaller than mid


left should be greater than mid
right should be greater than mid

"""
"""
nums.sort()
n = len(nums)
left = 0
right = n-1

res = []

res.append(nums[left])
left += 1

res.append(nums[right])
right -= 1

res.append(nums[left])

left += 1

while left < right:

    res.append(nums[right])
    right -= 1
    res.append(nums[left])

    left += 1

if n % 2  == 0:

    res.append(nums[left])

print(res)
"""
"""
first fill alternate blocks of res with smaller elements remaining element with larger
"""
nums.sort()
n = len(nums)
res = [0] * n

left = 0
right = n - 1
i = 0
while left <= right:

    if left % 2 == 0:

        res[i] = nums[left]

        left += 1

    else:

        res[i] = nums[right]

        right -= 1

    i += 1

print(res)