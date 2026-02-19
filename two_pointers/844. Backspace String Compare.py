"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

s = "bxj##tw"
t = "bxo#j##tw"

i = len(s)-1
j = len(t)-1

skip_i = 0
skip_j = 0

while i >= 0 or j >= 0:

    while i >= 0:

        if s[i] == "#":

            skip_i += 1
            i -= 1

        elif skip_i > 0:

            skip_i -= 1
            i -= 1

        else:
            break

    while j >= 0:

        if t[j] == "#":

            skip_j += 1
            j -= 1

        elif skip_j > 0:

            skip_j -= 1
            j -= 1

        else:
            break

    chr1  = s[i] if i >= 0 else "$"
    chr2 = t[j] if j >= 0 else "$"

    if chr2 != chr1 :
        print(False)
        exit()

    i -= 1
    j -= 1

print(True)