"""
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        low = 0
        high = len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]

            low += 1
            high -= 1

        return s