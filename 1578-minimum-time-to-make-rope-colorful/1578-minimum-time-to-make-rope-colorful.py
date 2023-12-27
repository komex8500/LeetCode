class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n < 3:
            return 0
        dp = [0] * n
        stack = [0]
        for i in range(1, n):
            if colors[stack[-1]] != colors[i]:
                stack.append(i)
                dp[i] = dp[i-1]
            else:
                if neededTime[stack[-1]] > neededTime[i]:
                    dp[i] = dp[i-1] + neededTime[i]
                else:
                    rm = stack.pop()
                    stack.append(i)
                    dp[i] = dp[i-1] + neededTime[rm]

        return dp[-1]