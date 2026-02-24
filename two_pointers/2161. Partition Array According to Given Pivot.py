""""You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement."""

nums = [-3,4,3,2];pivot = 2

n = len(nums)
res = [0]*n

left = 0
right = n-1

left_r = 0
right_r = n-1

while left < n:

    if nums[left] < pivot:

        res[left_r] = nums[left]

        left_r += 1

    if nums[right] > pivot:

        res[right_r] = nums[right]

        right_r -= 1

    left += 1
    right -= 1

while left_r <= right_r:

    res[left_r] = pivot
    res[right_r] = pivot

    left_r += 1
    right_r -= 1

print(res)