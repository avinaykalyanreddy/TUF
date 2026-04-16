"""
You are given a circular array nums and an array queries.

For each query i, you have to find the following:

The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
Return an array answer of the same size as queries, where answer[i] represents the result for query i.
"""
class Solution:
    def solveQueries(self, nums, queries) :
        dic = {}

        for idx,val in enumerate(nums):

            if val not in dic:

                dic[val] = []

            dic[val].append(idx)
        res = []

        for q_idx in queries:

            val  = nums[q_idx]

            dic_l = len(dic[val])
            low = 0
            high = dic_l-1
            arr = dic[val]

            if len(arr) == 1:

                res.append(-1)
                continue
            while low <= high:

                mid = (low+high)//2

                if arr[mid] == q_idx:

                    right = arr[(mid+1)% len(arr)]
                    left = arr[(mid-1)% len(arr)]

                    x = min((q_idx-left+len(nums))%len(nums),(q_idx-right+len(nums))%len(nums))
                    y = min((left-q_idx+len(nums))%len(nums),(right-q_idx+len(nums))%len(nums))

                    res.append(min(x,y))
                    break
                elif arr[mid] > q_idx:

                    high = mid-1

                else:

                    low = mid + 1



        return(res)