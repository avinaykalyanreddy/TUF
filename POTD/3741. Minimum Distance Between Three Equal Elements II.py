"""
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.


"""
nums = [1,1,2,3,2,1,2]
dic = {}

for idx,val in enumerate(nums):

    if val not in dic:

        dic[val] = []

    dic[val].append(idx)
res = float("inf")
for key in dic:
    l = len(dic[key])
    if l > 2:

        for  i in range(l-2):


            res = min(res,abs(dic[key][i] - dic[key][i+1])+abs(dic[key][i+1]-dic[key][i+2])+abs(dic[key][i]-dic[key][i+2]))

print(res)
