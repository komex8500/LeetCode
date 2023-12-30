class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = ("").join(words)
        for c in s:
            if s.count(c) % len(words) != 0:
                return False
        return True