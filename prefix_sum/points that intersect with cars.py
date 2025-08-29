nums = [[3,6],[1,5],[4,7]]


prefix = [0]*102 # swipe line

for s,e in nums:

    prefix[s] += 1
    prefix[e+1] -= 1

count = 0
cur = 0

for i in prefix:

    cur += i

    if cur > 0:

        count += 1

print(count)