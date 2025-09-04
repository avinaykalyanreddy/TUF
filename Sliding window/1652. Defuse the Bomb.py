"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
"""
code = [2,4,9,3]; k = -2

n = len(code)
res = [0] * n


total_sum = 0

if k > 0:

    left = 0

    for right in range(n+k):

        total_sum += code[(right)%n]

        if right - left + 1 == k + 1:

            total_sum -= code[left % n]

            res[left] = total_sum

            left += 1

elif k < 0:

    right = n-1

    for left in range(n-1,0+k-1,-1):

        total_sum += code[left]

        if left - right - 1 == k-1:

            total_sum -= code[right]

            res[right] = total_sum

            right = right - 1

print(res)