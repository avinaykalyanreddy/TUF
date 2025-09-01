colors = [0,1,0,1,0]; k = 3


res = 0
left = 0
n = len(colors)


for right in range(1,n+k-1):

    if colors[(right)%n] == colors[(right - 1)%n]:

        left = right

    if right - left + 1 > k:

        left = left + 1

    if right - left + 1 == k:

        res += 1

print(res)