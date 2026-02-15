"""
Given two binary strings a and b, return their sum as a binary string.
"""
a = "11";b = "1"

ptr1 = len(a)-1
ptr2 = len(b)-1
carry = 0
res = ""
while ptr1 >= 0 or ptr2 >= 0:

    val1 = a[ptr1] if ptr1 >= 0 else 0

    val2 = b[ptr2] if ptr2 >=0 else 0

    total = carry + int(val1 ) + int(val2)

    res = str(total % 2) + res

    carry = total//2

    ptr2 -= 1
    ptr1 -= 1

if carry :

    res = "1" + res

print(res)