class Solution:
    dp = [ [ 1 for _ in range(i+1) ] for i in range(100) ]
    for i in range(1, 100):
        for j in range(1, i+1):
            if i == j: dp[i][j] = 2 * dp[i][j-1]
            else: dp[i][j] = dp[i][j-1] + dp[i-1][j]

    def uniquePaths(self, m: int, n: int) -> int:
        if m < n: m, n = n, m
        return Solution.dp[m-1][n-1]
"""
if both i, j same just get 2*left
"""