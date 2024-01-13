class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_list = [0] * 26
        result = 0
        for c in s:
            s_list[ord(c) - ord('a')] += 1
        for c in t:
            if s_list[ord(c) - ord('a')] > 0:
                s_list[ord(c) - ord('a')] -= 1
            else:
                result += 1
        return result