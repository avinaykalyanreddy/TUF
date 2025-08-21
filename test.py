nums = [1, 1, 1, 2, 3, 4];k = 6




left = 0

res = 0

cur = 0

for right in range(len(nums)):

    cur += nums[right]

    while cur > k :

        cur = cur - nums[left]

        left += 1

    if cur == k:

        res = max(res,right-left+1)
        cur = cur - nums[left]
        left = left + 1

print(res)