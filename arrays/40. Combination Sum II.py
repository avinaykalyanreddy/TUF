"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


"""
candidates = [10,1,2,7,6,1,5];target = 8

candidates.sort()


lst = []
res = []
def backtrack(idx,total):

    if total > target:

        return

    if total == target:

        res.append(list(lst))
        return

    for i in range(idx,len(candidates)):

        if i > idx and candidates[i] == candidates[i-1]:

            continue
        lst.append(candidates[i])
        backtrack(i+1,total+candidates[i])

        lst.pop()

backtrack(0,0)

print(res)