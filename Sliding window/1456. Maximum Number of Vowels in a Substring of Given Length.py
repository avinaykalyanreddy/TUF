"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""
s = "abciiidef"; k = 3

vowels = {"a","e","i","o","u"}

left = 0
cnt = 0
res = 0

for right in range(len(s)):

    if s[right]  in vowels:

        cnt += 1

    if right - left + 1 > k :

        if s[left] in vowels:

            cnt -= 1

        left += 1

    res = max(res,cnt)

print(res)

