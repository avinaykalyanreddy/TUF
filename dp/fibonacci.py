
n = 5

""" recursive solution
def fibonacci(n):

    if n <= 1:

        return n

    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(n))
"""

dic  = {}
def fibonacci(n): # top-down or memoization

    if n <= 1:

        return n

    if n in dic:

        return dic[n]

    dic[n] = fibonacci(n-1)+fibonacci(n-2)

    return dic[n]
fibonacci(n)
print(dic)