class Solution:
    dp = [ [ 1 for _ in range(100) ] for _ in range(100) ]
    for i in range(1, 100):
        for j in range(1, 100):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    def uniquePaths(self, m: int, n: int) -> int:
        return Solution.dp[m-1][n-1]
"""

"""