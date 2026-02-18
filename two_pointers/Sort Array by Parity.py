"""
You are given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


class Solution:
    def sortArrayByParity(self, nums) :

        left = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        return nums