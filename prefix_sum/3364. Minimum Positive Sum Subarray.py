nums = [1, 2, 3, 4]
l = 2
r = 4

n = len(nums)

prefix = [0]

for i in range(n):

    prefix.append(prefix[-1]+nums[i])

print(prefix)