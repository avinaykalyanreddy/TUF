nums = [2,10,7,5,4,1,8,6]


min_idx = nums.index(min(nums))

max_idx = nums.index(max(nums))

n = len(nums)

left = max(min_idx,max_idx)+1

right = max(n-min_idx,n-max_idx)


both = min(min_idx,max_idx)+1 + min(n-min_idx,n-max_idx)


print(min(left,right,both))