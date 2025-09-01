nums = [87063,61094,44530,21297,95857,93551,9918]; k = 6


nums.sort()

res  = float("inf")
n = len(nums)
left = 0

for right in range(n):

    if right - left + 1 == k:

        res = min(res,nums[right] - nums[left])

        left = left + 1

print(res)