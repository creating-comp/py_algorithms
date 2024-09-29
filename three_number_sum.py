def three_sum(arr, target):
    arr.sort()
    pair = []
    for i in range(len(arr)-1):
        left = i+1
        right = len(arr)-1
        current = arr[i]  
        while left < right:
            if arr[left] + arr[right] + current < target:
                left += 1
            elif arr[left] + arr[right] + current > target:
                right -=1
            else:
                pair.append([arr[right], arr[left], current])
                left += 1
                
    for i in pair:
        if pair.count(i) > 1:
            pair.remove(i)
    return pair
