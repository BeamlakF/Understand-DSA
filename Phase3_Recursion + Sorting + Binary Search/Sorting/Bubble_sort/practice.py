def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # TODO 2: Create an inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            if arr[j]>arr[j+1]:
                arr[j] = arr[j+1]
            
