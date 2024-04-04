#hashing
from collections import defaultdict

def bolen(sayi):
    arr = []
    if sayi == 1:
        arr.append(1)
    for i in range(1, sayi):
        if sayi % i == 0:
          arr.append(i)
    return arr

def a_pair():
    d = defaultdict(list)
    s = 0
    for i in range(1, 10000):
        a = bolen(i)
        d[i].append(sum(a))
    for i in range(1, 10000):
        if d[i] != [i] and d[i][0] < 10000 and d[d[i][0]][0] == i:
            s += i
    print(s)
a_pair()
