"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""
cost  = [1,100,1,1,1,100,1,1,100,1]

n = len(cost)
dic = {}

def top(idx):

    if idx >= n:

        return 0

    if idx not in dic:

        dic[idx] = cost[idx]+min(top(idx+1),top(idx+2))

    if idx == 0:

        return min(dic[0],dic[1])

    return dic[idx]

print(top(0))