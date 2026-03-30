"""
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.


"""
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = [0]*26
        even2 = [0]*26

        odd1 = [0]*26
        odd2 = [0]*26

        def build(s,e,o):

            for i,j in enumerate(s):

                if i % 2 == 0:

                    e[ord(j)-ord('a')] += 1

                else:

                    o[ord(j) - ord('a')] += 1

        build(s1,even1,odd1)
        build(s2,even2,odd2)

        return even1 == even2 and odd1 == odd2