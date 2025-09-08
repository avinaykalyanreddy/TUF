"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""

n = 1; trust = []

count = [0]*n

for f,t in trust:

    count[f-1] -= 1
    count[t-1] += 1


for i in range(n):

    if count[i] == n-1:

        print(i+1)
        exit()

print(-1)