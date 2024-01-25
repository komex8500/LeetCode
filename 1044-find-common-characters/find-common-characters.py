class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = [[0] * len(words) for _ in range(26)]
        ans = []
        for j in range(len(words)):
            for k in range(len(words[j])):
                count[ord(words[j][k])-ord('a')][j] += 1
        for i in range(26):
            for _ in range(min(count[i])):
                ans.append(chr(i+97))
        return ans