"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

n = 5

dic = {}
def climbing(n):

    if n <= 0:

        if n == 0:
            return 1

        return 0

    if n not in dic:

        dic[n] = climbing(n-1)+climbing(n-2)

    return dic[n]

print(climbing(n))