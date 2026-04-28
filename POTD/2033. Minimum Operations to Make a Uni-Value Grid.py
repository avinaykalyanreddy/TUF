"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.


"""
grid = [[2,4],[6,8]]; x = 2


arr = []

for i in grid:

    arr.extend(i)

arr.sort()

val = arr[(len(arr)-1)//2]

res = 0

for i in arr:

    y = abs(val-i)

    if y % x == 0:


        res = res  + (y//x)

    else:

        print(-1)

print(res)