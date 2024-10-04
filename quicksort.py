def partition(arr, l, h):
    pivot = arr[h] 
    i = l - 1

    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1  

def quick_sort(arr, l,h):
    if l < h:
        
        p = partition(arr, l,h)

        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1,h)

def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

print("Unsorted array:")
print_array(arr)

quick_sort(arr, 0, n - 1)

print("Sorted array:")
print_array(arr)
