arr = arr = [3]


stack = []

n = len(arr)

for i in range(n-1,-1,-1):

    if not stack:

        stack.append((arr[i],i))

    elif arr[i] > stack[-1][0]:

        stack.append((arr[i],i))

for i in range(n):

    idx = stack[-1][1]

    if idx == i:

        stack.pop()

    if not stack:

        arr[i] = -1

    else:

        val = stack[-1][0]

        arr[i]  = val

print(arr)