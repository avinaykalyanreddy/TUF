
```python
arr = [3,1,2,4,1,5,2,6,4]

def sort(pivot, low, high):

    i = low
    j = high

    while i <= j : # j should cross the i

        while arr[i] <= arr[pivot] and  i <= high:

            i += 1


        while arr[j] > arr[pivot] and j >= low:

            j = j - 1

        if i <= j:

            arr[i],arr[j] = arr[j],arr[i]

            i += 1
            j -= 1





    arr[pivot],arr[j] = arr[j],arr[pivot]

    return j


def quick_sort(low,high):

    if low >= high:

        return

    pivot = sort(low,low+1,high)

    quick_sort(low,pivot-1)
    quick_sort(pivot+1,high)


quick_sort(0,len(arr)-1)

print(arr)
```
