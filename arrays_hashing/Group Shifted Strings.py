import collections

strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

dic = collections.defaultdict(list)

for i in strings:


    if len(i) == 1:

        dic[(-1,)].append(i)

    else:

        lst = []

        for a,b in zip(i,i[1::]):

            lst.append((ord(b)-ord(a))%26)

        dic[tuple(lst)].append(i)

print(list(dic.values()))