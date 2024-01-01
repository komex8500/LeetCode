class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        s_index = 0
        g_index = 0
        g.sort()
        s.sort()
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                result += 1
                s_index += 1
                g_index += 1
            else:
                s_index += 1
        return result