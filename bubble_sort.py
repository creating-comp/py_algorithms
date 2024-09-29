def bubble(arr):
    n = len(arr)
    while arr != sorted(arr):
        for i in range(n-1):
            tmp = 0
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    return arr
print(bubble([5, 3, 8, 4, 6]))
