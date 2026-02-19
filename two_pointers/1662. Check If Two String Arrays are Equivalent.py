"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""
word1 = ["ab", "c"]; word2 = ["a", "bc"]


idx1 = len(word1[-1])-1

idx2 = len(word2[-1])-1

len1 = len(word1)-1
len2 = len(word2)-1

while len1 >= 0  and len2 >= 0:

    w1 = word1[len1]
    w2 = word2[len2]



    while idx1 >= 0 and idx2 >= 0:

        if word1[len1][idx1] != word2[len2][idx2]:
            print(False)
            exit()

        idx1 -= 1
        idx2 -= 1

    if idx1 < 0 :

        len1 -= 1
        idx1 = len(word1[len1]) - 1

    if idx2 < 0 :

        len2 -= 1

        idx2 = len(word2[len2]) - 1
print(len2 == len1)

