"""
Problem Restated in Simple Words:

You have n teams (0 to n-1).

You’re given a DAG (Directed Acyclic Graph) that shows who is stronger than whom.

An edge [u, v] means team u is stronger than team v.

A champion is a team that has no incoming edges → meaning no other team is stronger than it.

👉 If there is exactly one such team, return its number.
👉 If there are zero or more than one, return -1.
"""

n = 4; edges = [[0,2],[1,3],[1,2]]

res = [0]*n

for f,t in edges:

    res[t] += 1



cnt = 0
idx = -1

for i,j in enumerate(res):

    if j == 0:

        cnt += 1
        idx = i


if cnt == 1:

    print(idx)

else:

    print(-1)