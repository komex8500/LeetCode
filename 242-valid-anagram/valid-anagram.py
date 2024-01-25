class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            if count[ord(c) - ord('a')] == 0:
                return False
            count[ord(c) - ord('a')] -= 1
        return True if sum(count) == 0 else False
