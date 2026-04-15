"""
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

"""
words = ["hello","i","am","leetcode","hello"];target = "hello";startIndex = 1


l = len(words)

res = float("inf")

def shortest_dis(idx):

    i = startIndex
    checker = True
    res = 0

    while checker or i != startIndex:

        if i == startIndex:

            checker = False

        if words[i] == target:
            return res

        i = (i+idx)%l
        res += 1

    return float("inf")


res = min(res,shortest_dis(1))
res = min(res,shortest_dis(-1))

print(res)
