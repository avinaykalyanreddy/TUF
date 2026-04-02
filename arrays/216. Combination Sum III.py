"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""
k = 3;n = 9



lst = []

res = []
def backtracking(start,total):

    if total > n or len(lst) > k:

        return

    if total == n and len(lst) == k:

        res.append(list(lst))
        return
    for i in range(start,n):
        if i < 10:
            lst.append(i)
            backtracking(i+1,total+i)
            lst.pop()
backtracking(1,0)

print(res)