class Solution(object):
    def integerReplacement(self, n):
        s = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                if n == 3 or (n // 2) % 2 == 0:
                    n -= 1
                else:
                    n += 1
            s += 1
        return s
