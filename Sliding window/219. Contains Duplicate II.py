# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

nums = [1,2,3,1,2,3]; k = 2







"""
dic = {}
for idx,val in enumerate(nums):

    if val in dic:

        if abs(dic[val] - idx ) <= k:

            print(True)
            exit()

    dic[val] = idx


print(False)"""





""""
arr = sorted([(idx,val) for idx,val in enumerate(nums)],key=lambda a:a[1])
print(arr)
for i in range(len(arr)-1):

    if arr[i][1] == arr[i+1][1] and abs(arr[i][0] - arr[i+1][0]) <= k:

        print(True)


print(False)

"""

window = set()

left = 0

for right in range(len(nums)):

    if right - left > k : # window size should be k+1

        window.remove(nums[left])

        left += 1


    if nums[right] in window:

        print(True)


    window.add(nums[right])

print(False)

# space complexity O(k)
# time complexity O(n)