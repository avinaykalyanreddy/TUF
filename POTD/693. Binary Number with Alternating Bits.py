"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values
"""

n = 10

bit = n & 1

def checking(bit,n):

    while n:

        x = n & 1

        n = n >> 1

        if x == bit:

            bit = 0 if x == 1 else 1
            continue

        return False

    return True

print(checking(bit,n))