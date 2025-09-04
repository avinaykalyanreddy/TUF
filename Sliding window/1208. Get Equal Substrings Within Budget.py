"""
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
"""
s = "pxezla"; t = "loewbi"; maxCost = 25

left = 0
res = 0

total = 0

for right in range(len(s)):

    total += abs(ord(s[right]) - ord(t[right]))

    while total > maxCost:

        total -= abs(ord(s[left]) - ord(t[left]))

        left += 1

    if total <= maxCost :

        res = max(res,right - left + 1)

print(res)