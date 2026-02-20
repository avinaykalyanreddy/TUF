"""
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.
"""
s = "11011000"

def solve(s):

    start = 0
    x = []
    balance = 0

    for i in range(len(s)):

        balance += 1 if s[i] == '1' else -1

        if balance == 0:


            inner_part = solve(s[start+1:i])
            x.append('1'+inner_part+'0')

            start = i+1

    x.sort(reverse=True)

    return "".join(x)
print(solve(s))