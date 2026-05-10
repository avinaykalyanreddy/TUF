"""
You are given a string s of length n consisting of lowercase English letters.

Return the smallest index i such that s[i] == s[n - i - 1].

If no such index exists, return -1.


"""
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l = len(s)
        for idx,val in enumerate(s):

            if s[l-1-idx] == val:

                return(idx)

        return -1