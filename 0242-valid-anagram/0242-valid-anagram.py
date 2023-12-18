

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0 for _ in range(26)]
        for i in s:
            letters[ord(i) - 97] += 1
        for i in t:
            letters[ord(i) - 97] -= 1
        for i in range(26):
            if letters[i]:
                return False
        return True
