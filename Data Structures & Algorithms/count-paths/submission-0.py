class Solution:
    dp = [ [ 1 for _ in range(100) ] for _ in range(100) ]
    for i in range(1, 100):
        for j in range(1, 100):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    def uniquePaths(self, m: int, n: int) -> int:
        return Solution.dp[m-1][n-1]
"""
dp
100 x 100?
and return index

static 



test
1, 1, 1, 1, 1, 1
1, 2, 3, 4, 5, 6
1, 3, 6, 10, 15, 21


opt: 
use only j >= i (symmetry, m x n == n x m) 
"""