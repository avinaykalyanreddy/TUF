"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.


"""
nums  = ["00","01"]


unique = set(nums)

n = len(nums)

arr = []
def becktracking():

    if len(arr) == n:

        s = "".join(arr)

        return s if s not in unique else ""
    arr.append('0')
    left = becktracking()

    if arr:
        arr.pop()
    right = ""
    if left == "":
        arr.append('1')
        right = becktracking()
    if arr:
        arr.pop()
    return left if left else right




print(becktracking())