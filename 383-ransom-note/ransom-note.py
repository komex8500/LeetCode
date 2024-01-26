class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for c in magazine:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for c in ransomNote:
            if c not in d or d[c] < 1:
                return False
            else:
                d[c] -= 1
        return True
