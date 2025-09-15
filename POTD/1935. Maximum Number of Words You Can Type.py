text = "leet code"; brokenLetters = "lt"


check = True

res = 0
for i in text:

    if i == " ":

        if check:

            res += 1

        check = True

    elif i in brokenLetters:

        check = False

if check:

    res += 1

print(res)