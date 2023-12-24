class Solution:
    def minOperations(self, s: str) -> int:
        f0, f1 = 0, 0
        for i, c in enumerate(s):
            if (i % 2 == 1 and c == '0') or (i % 2 == 0 and c == '1'):
                f0 += 1
            else:
                f1 += 1
        return min(f0, f1)