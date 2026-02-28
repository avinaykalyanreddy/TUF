"""
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.


"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0

        for i in range(1, n + 1):
            res = ((res << i.bit_length()) + i) % (10 ** 9 + 7)

        return (res)