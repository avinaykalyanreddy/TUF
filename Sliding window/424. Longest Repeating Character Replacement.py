"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


"""

s = "AABABBA"; k = 1
"""
count = {}

res = 0

left = 0

for right in range(len(s)):

    count[s[right]] = 1 + count.get(s[right],0)


    while (right - left + 1) - max(count.values()) > k:

        count[s[right]] -= 1

        left += 1

    res = max(res,right - left + 1 )

print(res)

"""

count = {}
res = 0

left = 0

max_val = 0

for right in range(len(s)):

    count[s[right]] = 1 + count.get(s[right],0)
    max_val = max(max_val,count[s[right]])
    while (right - left +1) -  max_val > k:

        count[s[left]] -= 1

        left += 1

    res = max(res, right - left + 1)

print(res)