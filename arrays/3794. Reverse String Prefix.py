class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix = s[0:k]
        suffix = s[k::]

        return prefix[::-1] + suffix