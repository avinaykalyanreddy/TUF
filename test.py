nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; k = 3



res = 0

left = 0


cnt_zero = 0

for right in range(len(nums)):

    if nums[right] == 0:

        cnt_zero += 1

    while cnt_zero > k:

        if nums[left] == 0:

            cnt_zero -= 1

        left += 1

    res = max(res,right-left+1)

print(res)
