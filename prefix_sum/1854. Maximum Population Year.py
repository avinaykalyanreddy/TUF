# if the input is range for prefix sum then use swipe line technique

logs = [[2025,2041],[1988,2007],[2003,2046],[2045,2049],[2025,2027],[2014,2040],[2014,2027],[2011,2027],[1972,2019]]


prefix = [0] * 101

for birth, death in logs:

    if birth >= 2000:

        prefix[birth % 100 + 50] += 1

    else:

        prefix[birth % 100 - 50] += 1

    if death >= 2000:

        prefix[death % 100 + 50] -= 1

    else:

        prefix[death % 100 - 50] -= 1


res = float("-inf")

cur = 0
year = 0

for idx,i in enumerate(prefix):

    cur = cur + i

    if cur > 0:

        if cur > res:

            res = cur
            year = idx

print(1950 + year)
