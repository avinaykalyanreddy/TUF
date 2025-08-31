cardPoints = [96,90,41,82,39,74,64,50,30]; k = 8



n = len(cardPoints)

total = sum(cardPoints)

res = 0

sliding_window = n - k

partial_sum = 0

left = 0

for right in range(n):

    if right - left == sliding_window:
        res = max(res, total - partial_sum)
        partial_sum = partial_sum - cardPoints[left]

        left += 1



    partial_sum += cardPoints[right]


if right - left + 1 == sliding_window:
    res = max(res, total - partial_sum)



print(res)

