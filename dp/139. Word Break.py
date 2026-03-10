"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        seen = {}
        n = len(s)

        def recursion(idx):

            if idx in seen:
                return seen[idx]
            if idx == n:
                return True

            ans = False

            for wrd in wordDict:

                wn = len(wrd)

                if idx + wn <= n and s[idx:idx + wn] == wrd and not ans:
                    ans = recursion(idx + wn)
            seen[idx] = ans
            return ans

        return recursion(0)