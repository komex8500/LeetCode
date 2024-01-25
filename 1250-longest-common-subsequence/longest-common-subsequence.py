class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        if text1 == text2:
            return l1
        dp = [[0] * (l1+1) for _ in range(l2+1)]
        for j in range(1, l2+1):
            for k in range(1, l1+1):
                if text1[k-1] == text2[j-1]:
                    dp[j][k] = dp[j-1][k-1] + 1
                else:
                    dp[j][k] = max(dp[j-1][k], dp[j][k-1])
        return dp[-1][-1]