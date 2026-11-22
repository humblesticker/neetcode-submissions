class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N

        def prevMax(pos):
            pmax = 0
            for i in range(pos):
                if nums[i] < nums[pos]: pmax = max(pmax, dp[i])
            return pmax

        for i in range(N):
            dp[i] = prevMax(i) + 1

        return max(dp)

"""

"""