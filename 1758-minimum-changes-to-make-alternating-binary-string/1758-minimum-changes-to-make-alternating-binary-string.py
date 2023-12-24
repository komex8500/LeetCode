class Solution:
    def minOperations(self, s: str) -> int:
        if s[0] == '0':
            f0 = 0
            f1 = 1
        else:
            f0 = 1
            f1 = 0
        for i in range(1, len(s)):
            if i % 2 == 1:
                # '0' is first
                if s[i] == '0':
                    f0 += 1
                # '1' is first
                if s[i] == '1':
                    f1 += 1
            else:
                # '0' is first
                if s[i] == '1':
                    f0 += 1
                # '1' is first
                if s[i] == '0':
                    f1 += 1
        return min(f0, f1)