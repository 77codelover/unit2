def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                
arr = [1,23,3,45,6,4,67,90]
bubble_sort(arr)
for i in arr:
    print(i)