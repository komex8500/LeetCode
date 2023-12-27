class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n < 3:
            return 0
        result = 0
        i = 0
        j = 1
        while i < n and j < n:
            if colors[i] == colors[j]:
                if neededTime[i] > neededTime[j]:
                    result += neededTime[j]
                else:
                    result += neededTime[i]
                    i = j
            else:
                i = j
            j += 1
        return result