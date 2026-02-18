"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


"""

g = [10,9,8,7]
s = [5,6,7,8]

g.sort()
s.sort()
i = j = 0

while i < len(g):

    while j < len(s) and g[i] > s[j]:

        j += 1

    if j == len(s):

        break

    j += 1
    i += 1

print(i)