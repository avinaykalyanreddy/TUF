# output should be the unique of elements in  two arrays

arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,4,5,5,5,6]

n = len(arr1)
m = len(arr2)

i = 0
j = 0
res = []

while i < n and j < m :

    if arr1[i] <= arr2[j] :

        if len(res) == 0 or res[-1] != arr1[i]:

            res.append(arr1[i])

        i += 1

    else:

        if len(res) == 0 or res[-1] != arr2[j]:

            res.append(arr2[j])

        j += 1

while i < n:

    if len(res) == 0 or res[-1] != arr1[i]:

        res.append(arr1[i])

    i += 1



while  j < m:


    if len(res) == 0 or res[-1] != arr2[j]:

        res.append(arr2[j])

    j += 1

print(res)