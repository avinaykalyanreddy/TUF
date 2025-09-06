"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""
s = "aaaaaaaaaaaabbbbbcdd";t = "abcdd"
countT,window = {},{}

for i in t:

    countT[i] = countT.get(i,0)+1


res = [-1,-1]
min_len = float("inf")

have,need = 0,len(countT)

left = 0

for right in range(len(s)):

    c = s[right]

    window[c] = window.get(c,0) + 1

    if c in countT and window[c] == countT[c] :

        have += 1

    while have == need:

        if right - left + 1 < min_len:

            min_len = right - left + 1

            res = [left,right]

        window[s[left]] -= 1

        if s[left] in countT    and window[s[left]] < countT[s[left]]:

            have -= 1

        left += 1

print(res)