'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

s1 = "abc"; s2 = "lecaabee"

cnt1 = len(s1)

s1_count = {}

for i in s1:

    s1_count[i] = 1+s1_count.get(i,0)

s2_count = {}

left = 0

cnt2 = 0

for right in range(len(s2)):

    s2_count[s2[right]] = 1 + s2_count.get(s2[right],0)
    cnt2 += 1
    while   s2_count[s2[right]] > s1_count.get(s2[right],0):

        s2_count[s2[left]] -= 1

        left += 1
        cnt2 -= 1


    if cnt2 == cnt1:

        print(True)
        exit()

print(False)