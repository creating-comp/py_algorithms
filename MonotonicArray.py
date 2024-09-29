def isMonotonic(array):
    if len(array) == 0 or len(array) == 1:
            return True
    right = 1
    left = 0
    dec = 0
    inc = 0
    same = 0
    while right != len(array):
        if array[left] < array[right]:
            inc += 1
            right += 1
            left += 1
        elif array[left] > array[right]:
            dec += 1
            right += 1
            left += 1
        else:
            same += 1
            right += 1
            left += 1
    if inc + same == len(array)-1 or dec + same == len(array)-1:
        return True
    return False
