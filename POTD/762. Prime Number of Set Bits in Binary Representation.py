"""
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
"""

left = 10; right = 15



def check_prime(num):

    for i in range(2,int(num**0.5)+1):

        if num % i == 0:

            return False


    return True
res = 0
for i in range(left,right+1):

    cnt = 0
    while i:

        cnt = cnt + (i&1)

        i = i >> 1

    if cnt > 1 and check_prime(cnt):

        res += 1

print(res)