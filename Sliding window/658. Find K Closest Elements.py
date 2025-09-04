"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

"""

arr = [2,4,5,8]; k = 2; x = 6


res = [0,0]
val = float("inf")

total = 0

left = 0

for right in range(len(arr)):

    total = total + abs(arr[right]-x)
    if right - left + 1 > k:

        total = total - abs(arr[left] - x)

        left += 1

    if right - left + 1 == k:

        if total < val:

            val = total

            res[0] = left

            res[1] = right

lst = []

for i in range(res[0],res[1]+1):

    lst.append(arr[i])

print(lst)