"""
You are given an integer n.

A number is called digitorial if the sum of the factorials of its digits is equal to the number itself.

Determine whether any permutation of n (including the original order) forms a digitorial number.

Return true if such a permutation exists, otherwise return false.

Note:

The factorial of a non-negative integer x, denoted as x!, is the product of all positive integers less than or equal to x, and 0! = 1.
A permutation is a rearrangement of all the digits of a number that does not start with zero. Any arrangement starting with zero is invalid.
"""


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def factorial(n):
            res = 1
            for i in range(n, 0, -1):
                res = res * i

            return res

        dic1 = {}
        res = 0
        while n:

            x = n % 10

            dic1[x] = dic1.get(x, 0) + 1
            if n != 0:
                res = res + factorial(x)
            else:

                res = res + 1

            n = n // 10

        dic2 = {}

        while res:
            x = res % 10

            dic2[x] = dic2.get(x, 0) + 1

            res = res // 10

        return (dic2 == dic1)
