def smallestDifference(arrayOne, arrayTwo):
    point = 0
    val = abs(arrayOne[0] - arrayTwo[0])
    arr = []

    for i in arrayOne:
        while i != arrayOne[-1] and point != len(arrayTwo):
            if abs(arrayTwo[point] - i) < val:
                arr.clear()
                val = abs(arrayTwo[point] - i)
                arr.append(i)
                arr.append(arrayTwo[point])
                point += 1
            else:
                point += 1
        #i = arrayOne[-1] # It compared the 1st array with the 2nd array up to this point.
        point = 0
        while i == arrayOne[-1] and point != len(arrayTwo):
            if abs(arrayTwo[point] - i) < val:
                arr.clear()
                val = abs(arrayTwo[point] - i)
                arr.append(arrayOne[-1])
                arr.append(arrayTwo[point])
                point += 1
            else:
                point += 1

    return arr
