strs = strs = [""]


dic = {}

for i in strs:

    letters = [0]*26

    for j in i:

        letters[ord(j)-ord("a")] += 1

    letters = tuple(letters)
    if letters not in dic:

        dic[letters] = [i]
    else:

        dic[letters].append(i)

res = []

for i in dic:

    res.append(dic[i])

print(res)