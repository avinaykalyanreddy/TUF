prices = [7,1,5,3,6,4]

"""
stock market strategy buy low sell high
"""

min_val = float("inf")

res = 0

for i in prices:

    if i < min_val:


        min_val = i

    else:

        res = max(res,i - min_val)

print(res)