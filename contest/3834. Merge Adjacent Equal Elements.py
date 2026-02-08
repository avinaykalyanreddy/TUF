"""
You are given an integer array nums.

You must repeatedly apply the following merge operation until no more changes can be made:

If any two adjacent elements are equal, choose the leftmost such adjacent pair in the current array and replace them with a single element equal to their sum.
After each merge operation, the array size decreases by 1. Repeat the process on the updated array until no more changes can be made.

Return the final array after all possible merge operations.


"""


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        res = [nums[0]]

        n = len(nums)

        for i in range(1, n):

            if nums[i] == res[-1]:

                res[-1] = res[-1] + nums[i]

                while len(res) > 1 and res[-1] == res[-2]:
                    x = res.pop()

                    y = res.pop()

                    res.append(x + y)



            else:

                res.append(nums[i])

        return (res)