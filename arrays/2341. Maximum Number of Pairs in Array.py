"""You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

"""
nums = [1,3,2,1,3,2,2]

pairs = 0
single = 0

dic = {}

for i in nums:

    dic[i] = dic.get(i,0)+1

for i in dic:

    pairs += dic[i] // 2
    single += dic[i]%2

print(pairs,single)
