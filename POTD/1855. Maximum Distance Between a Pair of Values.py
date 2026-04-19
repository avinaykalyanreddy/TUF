"""
You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.


"""
nums1 = [55,30,5,4,2];nums2 = [100,20,10,10,5]

res = 0
n = len(nums1)
m = len(nums2)


for i in range(n):

    low = i
    high = m-1


    while low <= high:

        mid = (low+high)//2

        if nums1[i] <= nums2[mid]:

            res = max(res,mid-i)

            low = mid + 1

        else:

            high = mid - 1

print(res)