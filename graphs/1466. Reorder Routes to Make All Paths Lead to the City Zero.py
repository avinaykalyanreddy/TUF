"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""

# tip make bidirectional graph to get idea about how to solve and check ngbrs of 0 reaches to 0 or not

from collections import deque

n = 6; connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]


valid_nodes = set()
valid_nodes.add(0)
graph1 = {i: set() for i in range(n)}

for f,t in connections:

    graph1[f].add(t)


graph2 = {i : [] for i in range(n)}

for f,t in connections:

    graph2[f].append(t)
    graph2[t].append(f)

q = deque()
res = 0
for child in graph2[0]:

    q.append((child,0))

while q:

    child,parent = q.popleft()
    valid_nodes.add(parent)
    if parent not in  graph1[child]:

        res += 1
        valid_nodes.add(child)


    for ch in graph2[child]:
        if ch not in valid_nodes:
            q.append((ch,child))


print(res)

