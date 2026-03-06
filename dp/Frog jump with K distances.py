"""A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step, and an integer k.
to jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists.
Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.
"""
heights = [15, 4, 1, 14, 15];k = 3



n = len(heights)-1
seen = {}
def recursion(idx):


    if idx == n:

        return 0

    if idx in seen:

        return seen[idx]
    ans = float("inf")

    for i in range(idx+1,idx+k+1):

        if i <= n:

            ans  = min(abs(heights[i] - heights[idx]) + recursion(i),ans)

    seen[idx] = ans
    return seen[idx]

print(recursion(0))