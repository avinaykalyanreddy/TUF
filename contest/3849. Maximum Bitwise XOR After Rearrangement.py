"""
You are given two binary strings s and t​​​​​​​, each of length n.

You may rearrange the characters of t in any order, but s must remain unchanged.

Return a binary string of length n representing the maximum integer value obtainable by taking the bitwise XOR of s and rearranged t.
"""
from collections import deque


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        t = list(t)
        n = len(t)

        dq0 = deque([])

        for i in range(n):

            if t[i] == '0':
                dq0.append(i)

        dq1 = deque([])

        for i in range(n):

            if t[i] == '1':
                dq1.append(i)

        res = ""
        for i in range(n):

            while dq0 and dq0[0] < i:
                dq0.popleft()

            while dq1 and dq1[0] < i:
                dq1.popleft()

            if s[i] == t[i]:

                if t[i] == '0':
                    idx = i
                    if dq1:
                        idx = dq1.popleft()

                    t[i], t[idx] = t[idx], t[i]

                    if t[i] == '1':

                        res += '1'

                    else:
                        res += '0'

                else:

                    idx = i

                    if dq0:
                        idx = dq0.popleft()

                    t[i], t[idx] = t[idx], t[i]
                    if t[i] == '0':

                        res += '1'

                    else:

                        res += '0'

            else:

                res += '1'

        return (res)