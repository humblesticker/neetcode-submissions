class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = 1

        def prevMax(pos):
            pmax = 0
            for i in range(pos-1, -1, -1):
                if nums[i] < nums[pos]: pmax = max(pmax, dp[i])
            return pmax

        for i in range(1, N):
            dp[i] = prevMax(i) + 1

        return max(dp)

"""


dp
1 5 10 15 2 3
i, prev, dp
1, 1, 2
2, 2, 3
3, 3, 4
4, 1, 2
5, 2, 3

1 5 10 2 3 4
i, prev, dp
0, 0, 1
1, 1, 2
2, 2, 3
3, 1, 2
4, 2, 3
5, 3, 4

0,3,1,3,2,3
i, prev, dp
0, 0, 1
1, 1, 2
2, 1, 2
3, 2, 3
4, 2, 3
5, 3, 4

9,1,4,2,3,3,7
i, prev, dp
0, 0, 1
1, 0, 1
2, 1, 2
3, 1, 2
4, 2, 3
5, 2, 3
6, 3, 4

1 5 10 2 3 4
1(0), 2(3), 3(4), 4(5), 5(1), 10(2)

1 5 10 15 2 3 
1(0), 2(4), 3(5), 5(1), 10(2), 15(3)

sort 

1(1), 2(3), 3(4), 3(5), 4(2), 7(6), 9(0)
0(0), 1(2), 2(4), 3(1), 3(3), 3(5)
for each start find increased position and value
no need to look back


0,3,1,3,2,3

0, 1, 2, 3
"""