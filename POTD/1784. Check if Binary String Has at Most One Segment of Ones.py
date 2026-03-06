"""
Given a binary string without leading zeros, return true if s contains at most one contiguous segment of ones. Otherwise, return false.
"""

s = "110"

found = False

for i in range(len(s)):

    if s[i] == '1':

        found = True

        if i-1 > 0 and s[i] != s[i-1] and found:

            print(False)
            exit()
print(True)