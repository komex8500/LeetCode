class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        for i in range(len(s) - 1, len(s)//2 - 1, -1):
            index = s.find(s[i])
            result = max(result, (i - index - 1))
        return result