"""
Given an integer n, return the number of prime numbers that are strictly less than n.

"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:

            return 0
        def counting_prime(n):

            is_prime = [True]*(n+1)
            is_prime[0] = is_prime[1] = False
            i = 2

            for i in range(i,int(n**0.5)+1):

                if is_prime[i]:

                    for j in range(i*i,n+1,i):

                        is_prime[j] = False


            return  is_prime

        res = 0
        x = counting_prime(n)
        for i in range(len(x)-1):
            if x[i] :
                res = res + 1

        return res


