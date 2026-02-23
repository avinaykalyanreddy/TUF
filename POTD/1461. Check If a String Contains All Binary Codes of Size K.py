"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.


"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique = set()

        left = 0

        for right in range(len(s)):

            if right - left + 1 == k:

                unique.add(s[left:right+1])

                left += 1

        return(len(unique) == 2**k)
