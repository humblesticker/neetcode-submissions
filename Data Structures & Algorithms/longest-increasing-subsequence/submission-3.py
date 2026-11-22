class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N

        for i in range(N):
            pmax = 0
            for j in range(i):
                if nums[j] < nums[i]: pmax = max(pmax, dp[j])
            dp[i] = pmax + 1

        return max(dp)

"""

"""