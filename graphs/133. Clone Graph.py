adjList  = adjList = [[2,4],[1,3],[2,4],[1,3]]




class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2,n4]
n2.neighbors = [n1,n3]
n3.neighbors = [n2,n4]
n4.neighbors = [n1,n3]

visited = {}
def dfs(cur):

    if cur in visited:

        return visited[cur]

    copy = Node(cur.val)

    visited[cur] = copy

    for nbr in cur.neighbors:

        copy.neighbors.append(nbr)

    return visited[cur]


print(dfs(n1).neighbors)