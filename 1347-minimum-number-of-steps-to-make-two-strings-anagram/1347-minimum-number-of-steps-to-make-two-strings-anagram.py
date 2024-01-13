class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_list = [0] * 26
        t_list = [0] * 26
        result = 0
        for i in range(len(s)):
            s_list[ord(s[i]) - ord('a')] += 1
            t_list[ord(t[i]) - ord('a')] += 1
        for i in range(26):
            result += abs(s_list[i] - t_list[i])
        return result // 2