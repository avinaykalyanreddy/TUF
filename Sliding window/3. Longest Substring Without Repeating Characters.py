"Given a string s, find the length of the longest substring without duplicate characters."


s = "abcabcbb"

res = 0
left = 0

unique = set()

for right,val in enumerate(s):

    while s[right] in unique:

        unique.remove(s[left])

        left += 1

    unique.add(s[right])

    res = max(res,right - left + 1)

print(res)