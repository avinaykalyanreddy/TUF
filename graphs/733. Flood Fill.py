"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.


"""

image = [[1,1,1],[1,1,0],[1,0,1]]; sr = 1; sc = 1; color = 2

n = len(image)
m = len(image[0])
orginal_color = image[sr][sc]

def coloring(i,j):

    if 0 <= i < n and 0 <= j < m and image[i][j] != -1 and image[i][j] == orginal_color:

        image[i][j] = -1

        coloring(i+1,j)
        coloring(i-1,j)


        coloring(i,j+1)
        coloring(i,j-1)


    return

coloring(sr,sc)

for i in range(n):

    for j in range(m):

        if image[i][j] == -1:

            image[i][j]  = color


print(image)