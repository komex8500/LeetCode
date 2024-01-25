class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        return self.check_happy(n, s)

    def check_happy(self, n, s):
        if n == 1:
            return True
        if n in s:
            return False
        l = []
        new = 0
        s.add(n)
        for c in str(n):
            l.append(c)
        for i in range(len(l)):
            new += int(l[i]) ** 2
        return self.check_happy(new, s)