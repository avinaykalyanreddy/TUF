"""
You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.
"""
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def checking(s1,s2):

            lst1 = list(s1)

            left = 0
            right = 2

            while right < len(s1):
                if s1[right] != s2[right]:
                    lst1[left],lst1[right] = lst1[right],lst1[left]

                right += 1
                left += 1

            return "".join(lst1) == s2

        return checking(s1,s2) or checking(s2,s1)