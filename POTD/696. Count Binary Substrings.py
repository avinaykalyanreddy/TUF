"""
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""

s = "00110011"

res = 0

cnt1 = 1 #because index 0 dont have prev element so 1
cnt2 = 0

for i in range(1,len(s)):

    if s[i] == s[i-1]:

        cnt1 += 1

    else:

        res = res + min(cnt1,cnt2)

        cnt2 = cnt1
        cnt1 = 1

res = res + min(cnt1,cnt2)

print(res)