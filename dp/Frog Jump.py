"""
A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step.



To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from any step either one or two steps, provided it exists.



Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.
"""

heights  = [7, 5, 1, 2, 6]



n = len(heights)-1

seen = {}

def recursion(step):

    if step == n:

        return 0

    if step in seen:

        return seen[step]

    left = float("inf")
    right = float("inf")

    if step + 1 <= n:

        left = abs(heights[step]-heights[step+1]) + recursion(step+1)

    if step + 2 <= n:

        right = abs(heights[step] - heights[step+2]) + recursion(step+2)

    seen[step] = min(left,right)

    return seen[step]

print(recursion(0))