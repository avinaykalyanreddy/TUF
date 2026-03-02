"""
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).


"""
grid = [
    [1,0,0,0,0,0],
    [0,1,0,1,0,0],
    [1,0,0,0,0,0],
    [1,1,1,0,0,0],
    [1,1,0,1,0,0],
    [1,0,0,0,0,0]
]

zeros = []

n = len(grid)

for row in grid:
    x = 0
    for i in range(n-1,-1,-1):

        if row[i] == 0:

            x += 1

            continue
        break

    zeros.append(x)

print(zeros)
res = 0
for i in range(n):

    required = n - i - 1

    j = i
    while j < n and zeros[j] < required:

        j += 1

    if j == n:

        print(-1)
        exit()

    while j > i:

        zeros[j],zeros[j-1] = zeros[j-1],zeros[j]

        res += 1
        j -= 1
print(zeros)
print(res)