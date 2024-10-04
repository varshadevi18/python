def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    L = arr[l:l + n1]
    R = arr[m + 1:m + 1 + n2]

    i = 0  
    j = 0  
    k = l  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
  
    if l < r:
        
        m = l + (r - l) // 2

       
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

      
        merge(arr, l, m, r)


arr = [25, 10, 2, 9]
n = len(arr)

print("Unsorted array:")
print(arr)

merge_sort(arr, 0, n - 1)

print("Sorted array:")
print(arr)
