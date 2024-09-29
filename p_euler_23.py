from collections import defaultdict
def bolen(sayi):
    arr = []
    for i in range(1, sayi//2 + 1):
        if sayi % i == 0:
          arr.append(i)
    return sum(arr)

def abund():
    ab = []
    s = 0
    for i in range(1, 28123):
        if bolen(i) > i:
            ab.append(i)

    for i in range(28123):
        if not any((i - a in ab) for a in ab):
            s += i
    print(s)
abund()
