"""
You are given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

nums = [10,9,1,1,1,2,3,1]

"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(arr):

            n = len(arr)

            if n <= 1:

                return arr

            mid = n//2

            left = sort(arr[0:mid])
            right = sort(arr[mid::])


            i = 0
            j = 0
            res = []
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:

                    res.append(left[i])
                    i += 1

                else:

                    res.append(right[j])
                    j += 1


            while i < len(left):

                res.append(left[i])
                i += 1

            while j < len(right):

                res.append(right[j])

                j += 1

            return res



        return (sort(nums))