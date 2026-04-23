"""
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

"""


class Solution:
    def distance(self, nums) :

        dic = {}
        prefix = 0
        res = [0] * len(nums)
        for i, j in enumerate(nums):

            if j not in dic:
                dic[j] = [i]

            else:

                dic[j].append(dic[j][-1] + i)

        cnt = {}
        for i in range(len(nums)):

            val = nums[i]

            if len(dic[val]) != 1:

                if val not in cnt:
                    cnt[val] = 0

                cnt[val] += 1
                cur_idx = cnt[val] - 1

                l = len(dic[val])
                left_sum = 0
                right_sum = 0
                if cur_idx == 0:
                    print((l - 1) * val, val)
                    left_sum = abs((dic[val][-1] - dic[val][0]) - ((l - 1) * dic[val][0]))

                elif cur_idx == l - 1:

                    right_sum = abs(dic[val][-2] - (cnt[val] - 1) * (dic[val][-1] - dic[val][-2]))

                else:
                    value = dic[val][cur_idx] - dic[val][cur_idx - 1]
                    left_sum = abs(dic[val][cur_idx - 1] - (cur_idx * value))

                    right_sum = abs((dic[val][-1] - dic[val][cur_idx]) - (l - cur_idx - 1) * value)

                res[i] = left_sum + right_sum

        return res






