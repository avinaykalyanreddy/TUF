s = "pwwkew"

res = 0

unique = set()

left = 0
for right,val in enumerate(s):

    while val in unique:

        unique.remove(s[left])
        left += 1

    unique.add(val)

    res = max(res,right - left + 1)

print(res)