"""
You are given a string s that consists of lowercase English letters.

Return the string obtained by removing all trailing vowels from s.

The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.

"""


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s)
        seen = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n - 1, -1, -1):

            if s[i] not in seen:
                return (s[0:i + 1])

        return ""

