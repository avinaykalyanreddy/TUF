"""
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.
"""

s = "abbac"

n = len(s)

res = 0

for i in range(n):

    dic  = {}
    mf = 0
    for j in range(i,n):

        dic[s[j]] = dic.get(s[j],0)+1

        mf = max(dic[s[j]],mf)

        if mf * len(dic) == j-i+1: # when all frequencies are eqaul then max_freq * len(dic) == j-i+1

            res  = max(res,j-i+1)

print(res)