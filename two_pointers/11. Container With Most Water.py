height = [1,8,6,2,5,4,8,3,7]

low = 0
high = len(height)-1

res = 0

while low < high:

    area = min(height[low],height[high])*(high-low)

    res = max(res,area)

    if height[low] <= height[high]:

        low += 1

    else:

        high -= 1

print(res)