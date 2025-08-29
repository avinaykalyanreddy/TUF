# note if the input is range for prefix sum then use swipe line technique
ranges = [[1,10],[10,20]];left = 21;right = 21


prefix = [0]*52 # swipe line


for s,e in ranges:

    prefix[s] += 1
    prefix[e+1] -= 1

cnt = 0

cur = 0

print(prefix)

for i in range(len(prefix)):

    cur = cur + prefix[i]

    if cur > 0 and left <= i <= right:

        cnt += 1

print(cnt >= right - left + 1)