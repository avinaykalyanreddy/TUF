weights = [2, 3, 4]
values  = [4, 5, 7]
capacity = 5
n = len(weights)

seen = {}

def recursion(idx,wt):

    if idx == n:

        return 0


    if (idx,wt) in seen:

        return seen[(idx,wt)]
    left = 0

    if wt + weights[idx] <= capacity:

        left = values[idx] + recursion(idx+1,wt+weights[idx])

    right = recursion(idx+1,wt)

    seen[(idx,wt)] = max(left,right)

    return seen[(idx,wt)]

print(recursion(0,0))