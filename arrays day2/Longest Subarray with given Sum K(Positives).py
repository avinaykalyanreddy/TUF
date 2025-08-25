nums = [2,3,5,1,9]; k = 10

res = 0
"""
it is like pattern
2
2 3
2 3 5

where adding last element with cur sum

for i in range(len(nums)):
    cur = 0
    for j in range(i,len(nums)):

       cur = cur + nums[j]

       if cur == k:

           res = max(res,j-i+1)
print(res)

"""
# this code only works when array contains positive and zeros only

n = len(nums)

left = 0
cur = 0

for right in range(n):

    cur = cur + nums[right]

    while left <= right and  cur > k:

        cur = cur - nums[left]
        left += 1

    if cur == k:

        res = max(res,right-left+1)

print(res)