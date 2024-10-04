def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x  

arr = [18, 90, 5, 7, 14]
insertion_sort(arr)
print("Sorted array:", arr)
