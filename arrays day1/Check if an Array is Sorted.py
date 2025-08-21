
def check_sorted(arr):
    inc = True
    dec = True
    for i in range(len(arr)-1):


        if arr[i] > arr[i+1]:

            inc = False

        if arr[i] < arr[i+1]:

            dec = False

    if inc :

        return "Increasing"

    elif dec:

        return "Decreasing"

    else:

        return "unsorted"

print(check_sorted([4,3,2,2,1]))