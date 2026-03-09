"""
You are given a binary string s and two integers encCost and flatCost.

For each index i, s[i] = '1' indicates that the ith element is sensitive, and s[i] = '0' indicates that it is not.

The string must be partitioned into segments. Initially, the entire string forms a single segment.

For a segment of length L containing X sensitive elements:

If X = 0, the cost is flatCost.
If X > 0, the cost is L * X * encCost.
If a segment has even length, you may split it into two contiguous segments of equal length and the cost of this split is the sum of costs of the resulting segments.

Return an integer denoting the minimum possible total cost over all valid partitions.


"""

s = "00"; encCost = 1;flatCost = 2

seen = {}
def recursion(val):

    ones = val.count('1')
    n = len(val)

    if val in seen:

        return seen[val]


    if n % 2 == 1:

        if ones > 0:

            return n*ones*encCost
        return flatCost


    fs = n*ones*encCost if ones > 0 else flatCost
    mid = n//2

    right = recursion(val[:mid])
    left = recursion(val[mid:])


    seen[val] = min(fs,right+left)

    return seen[val]



print(recursion(s))