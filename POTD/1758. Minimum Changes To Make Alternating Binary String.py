"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""
s = "0100"

def checking(expected):

    flips = 0

    for i in s:

        if i != expected:

            flips += 1

        expected = '0' if expected == '1' else '1'

    return flips

print(min(checking('0'),checking('1')))