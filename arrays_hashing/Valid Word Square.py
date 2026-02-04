words = ["abc","b"]
"""
#space complexity O(1)
n = len(words)
try:
        for i in range(n):

             j = 0

             for l in words[i]:

                     if words[j][i] != l:

                             print(False)
                             exit()

                     j += 1

except:

        print(False)


print(True)
"""
#space complexity O(m*n)
new_row = 0

for i in words:

        new_row = max(new_row,len(i))

new_matrix=[]

for i in words:

        new_matrix.append("".join(i+"."*(new_row-len(i))))

if new_row != len(new_matrix):
        print(False)
        exit()
for i in range(new_row):

        j = 0

        for l in new_matrix[i]:

                if new_matrix[j][i] != l:

                        print(False)
                        exit()

                j += 1

print(True)
