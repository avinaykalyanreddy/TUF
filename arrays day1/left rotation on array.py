nums = [1, 2, 3, 4, 5]
k = 1
n = len(nums)
end = k % n


def reverse_left (low,high):

    while low < high:

        nums[low],nums[high] = nums[high],nums[low]

        low += 1

        high -= 1


reverse_left(0,end-1)
reverse_left(end,n-1)
reverse_left(0,n-1)

print(nums)