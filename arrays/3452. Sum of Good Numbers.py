"""
Given an array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist). If neither of these indices exists, nums[i] is still considered good.

Return the sum of all the good elements in the array.


"""
nums = [16,25,36];k = 1

l = len(nums)
res = 0
for i in range(l):

   if i-k >= 0 and i+k <= l-1 :
      if nums[i] > nums[i+k] and nums[i] > nums[i-k]:

          res = res+nums[i]

   elif i < k and i+k <= l-1 and nums[i] > nums[i+k]:
       res += nums[i]


   elif i>= l-k-1 and i-k >= 0 and  nums[i] > nums[i-k]:

       res += nums[i]

print(res)