"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
"""

s = "aabaaaacaabc";k = 2

count = [0,0,0]

for i in s:

    count[ord(i)  - ord("a")] += 1

if min(count) < k:

    print(-1)


left = 0
x = float("-inf")

for right in range(len(s)):

    count[ord(s[right]) - ord("a")] -= 1

    while min(count) < k:
        count[ord(s[left]) - ord("a")] += 1

        left += 1

    x = max(x,right - left +1)

print(len(s) - x)

