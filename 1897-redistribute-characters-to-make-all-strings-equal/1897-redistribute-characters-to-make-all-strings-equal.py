class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = dict()
        for word in words:
            for c in word:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
        for count in list(d.values()):
            if count % len(words) != 0:
                return False
        return True