def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i  
        for j in range(i + 1, len(lst)):  
            if lst[j] < lst[min_index]:
                min_index = j  
        
        lst[i], lst[min_index] = lst[min_index], lst[i]
    print("Sorted list =", lst)

selection_sort([18, 90, 5, 7, 14])
