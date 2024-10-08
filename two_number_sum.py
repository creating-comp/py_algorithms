def two_sum(arr, target):
    right = len(arr)-1
    left = 0
    arr.sort()
    pair = []
    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -=1
        else:
            pair.append([arr[right], arr[left]])
            left += 1
            right -=1
    return pair
