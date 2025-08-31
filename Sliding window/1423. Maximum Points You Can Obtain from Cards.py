"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""

# read give hint to find the sliding window
# sliding window formula = n-k

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

