"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
"""

s = "abc"

n = len(s)
left = 0

res = 0

dic = {}

for right in range(n):

    dic[s[right]] = 1 + dic.get(s[right],0)

    while len(dic) == 3:

        res = res + 1 + (n-1-right)

        dic[s[left]] -=  1

        if dic[s[left]] == 0:

            del dic[s[left]]

        left += 1

print(res)
