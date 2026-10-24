class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp1, dp2 = [1] * n, [1] * n

        for i in range(1, m):
            dp1, dp2 = dp2, dp1

            for j in range(1, n):
                dp2[j] = dp2[j-1] + dp1[j]

        return dp2[-1]
"""
m=7, n=3
dp1 [ 1, 3, 6 ]
dp2 [ 1, 2, 3 ]
i, j 
1, 
2,  
3

"""