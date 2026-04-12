"""You are given an integer n. We say that two integers x and y form a prime number pair if:

1 <= x <= y <= n
x + y == n
x and y are prime numbers
Return the 2D sorted list of prime number pairs [xi, yi]. The list should be sorted in increasing order of xi. If there are no prime number pairs at all, return an empty array.

Note: A prime number is a natural number greater than 1 with only two factors, itself and 1."""


class Solution:
    def findPrimePairs(self, n: int) :
        if n < 2:
            return []

        def counting_prime(n):

            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            i = 2

            for i in range(i, int(n ** 0.5) + 2):

                if is_prime[i]:

                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            return is_prime

        res = []
        primes = counting_prime(n)

        for i in range(2, n // 2 + 1):

            if primes[i] and primes[n - i]:
                res.append([i, n - i])

        return res

