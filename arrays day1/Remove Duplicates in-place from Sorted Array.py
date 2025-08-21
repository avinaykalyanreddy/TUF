nums = [1,1,2]

left = 1

res = 1

for i in range(1,len(nums)):

    if nums[i-1]  != nums[i]:

        nums[left] = nums[i]
        left += 1
        res += 1
print(res)
