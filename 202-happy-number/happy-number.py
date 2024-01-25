class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        return self.check_happy(n, s)

    def check_happy(self, n, s):
        l = []
        new = 0
        s.add(n)
        for c in str(n):
            l.append(c)
        for i in range(len(l)):
            new += int(l[i]) ** 2
        if new == 1:
            return True
        if new in s:
            return False
        return self.check_happy(new, s)