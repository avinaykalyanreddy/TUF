nums  = [7, 7, 8, 9, 10, 10]

m1 = float("inf")
m2  = float("inf")
ma1 = float("-inf")
ma2 = float("-inf")

for i in nums:

    if i < m1:

        m2 = m1

        m1 = i

    elif i < m2 and i != m1:

        m2 = i


    if i > ma1:

        ma2 = ma1
        ma1 = i

    elif i > ma2 and i != ma1:

        ma2 = i


print(m2) if m2 != float("inf") else print(-1)

print(ma2) if ma2 != float("-inf") else print(-1)