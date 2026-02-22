"""
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.



"""


class Solution:
    def binaryGap(self, n: int) -> int:
        low = -1
        high = 0

        res = 0

        while n:

            bit = n & 1
            if bit == 1:

                if low == -1:
                    low = high

                res = max(res, high - low)

                low = high

            high = high + 1

            n = n >> 1

        return (res)

