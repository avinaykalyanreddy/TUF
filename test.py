customers = [1,2,3];
grumpy = [1,1,0];
minutes = 1

n = len(customers)


left = 0

satisfied = 0

window = max_window = 0

for right in range(n):

    if grumpy[right] :

        window += customers[right]

    else:

        satisfied += customers[right]

    max_window = max(max_window, window)
    if right - left  ==  minutes:

        if grumpy[left]:

            window -= customers[left]

        left += 1

print(satisfied,window)