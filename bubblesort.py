def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [8, 90, 65, 7, 25]
bubble_sort(arr)
print("Sorted array:", arr)
