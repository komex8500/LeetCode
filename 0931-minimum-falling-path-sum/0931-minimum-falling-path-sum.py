class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]
        for j in range(1, n):
            for k in range(n):
                if k == 0:
                    dp[j][k] = min(dp[j-1][k], dp[j-1][k+1]) + matrix[j][k]
                elif k == n-1:
                    dp[j][k] = min(dp[j-1][k-1], dp[j-1][k]) + matrix[j][k]
                else:
                    dp[j][k] = min(dp[j-1][k-1], dp[j-1][k], dp[j-1][k+1]) + matrix[j][k]
        return min(dp[n-1])
        